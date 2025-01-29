"""
This is a simple FastAPI application that returns my email,
the current time and the URL to the github repository
"""

from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

email = "ucodimmegwa@gmail.com"
github_url = "https://github.com/VikingVik123/HNG12_Backend.git"

@app.get("/stats")
async def fetch_details():
    return {"email": email, "current_datetime": datetime.now().isoformat(), "github": github_url}