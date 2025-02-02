from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n: int) -> bool:
    """Check if a number is a perfect number."""
    return n > 0 and sum(i for i in range(1, n) if n % i == 0) == n

def digit_sum(n: int) -> int:
    """Calculate the sum of the digits of a number."""
    return sum(int(digit) for digit in str(n))

def is_armstrong(n: int) -> list:
    """Check if a number is an Armstrong number."""
    digits = [int(digit) for digit in str(n)]
    is_armstrong = n == sum(digit ** len(digits) for digit in digits)
    parity = "odd" if n % 2 != 0 else "even"
    return ["armstrong" if is_armstrong else "not armstrong", parity]

@app.get("/")
async def get_number_details(x: int):
    """Get details of a number."""

    url =  f"http://numbersapi.com/{x}"
    number = x
    sum = digit_sum(x)
    try:
        fun_fact = requests.get(url).text  # Get text from API response
    except requests.RequestException:
        fun_fact = "Error fetching fact"

    return JSONResponse(content={"number": number, 
                                 "is_prime": is_prime(x),
                                 "is_perfect": is_perfect(x),
                                 "properties": is_armstrong(x),
                                 "digit_sum": sum,
                                 "fun_fact": fun_fact})