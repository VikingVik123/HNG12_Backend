from flask import Flask, jsonify, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n <= 1:
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
    return sum(int(digit) for digit in str(abs(n)))  # sum digits of absolute value to avoid issues with negative signs

def is_armstrong(n: int) -> list:
    """Check if a number is an Armstrong number and return the appropriate properties."""
    abs_n = abs(n)  # Work with absolute value for the Armstrong check
    digits = [int(digit) for digit in str(abs_n)]  # work with absolute value of n
    is_armstrong = n == sum(digit ** len(digits) for digit in digits)
    parity = "odd" if n % 2 != 0 else "even"
    
    result = []
    if is_armstrong:
        result.append("armstrong")
    result.append(parity)
    
    return result

@app.route("/api/classify-number", methods=["GET"])
def get_number_details():
    """Get details of a number."""
    number = request.args.get('number')
    
    if number is None:
        return jsonify({"number": "alphabet", "error": True}), 400
    
    try:
        x = int(number)
    except ValueError:
        return jsonify({"number": number, "error": True}), 400

    # No absolute value here to preserve the sign
    original_number = x
    url = f"http://numbersapi.com/{abs(x)}"  # Pass the absolute value for the fun fact request
    sum_of_digits = digit_sum(x)
    
    try:
        fun_fact = requests.get(url).text
    except requests.RequestException:
        fun_fact = "Error fetching fact"

    return jsonify({
        "number": original_number,  # Return the original number, not the absolute value
        "is_prime": is_prime(x),
        "is_perfect": is_perfect(x),
        "properties": is_armstrong(x),
        "digit_sum": sum_of_digits,
        "fun_fact": fun_fact
    })

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
