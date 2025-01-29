"""
This is a simple FastAPI application that returns my email,
the current time and the URL to the github repository
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

email = "ucodimmegwa@gmail.com"
github_url = "https://github.com/VikingVik123/HNG12_Backend"

@app.get("/")
async def fetch_details():
    return {"email": email, "current_datetime": datetime.now().isoformat() + "Z", "github": github_url}