# Task Description

Develop a public API that returns the following information in JSON format:

1. Your registered email address (used to register on the HNG12 Slack workspace).
2. The current datetime as an ISO 8601 formatted timestamp.
3. The GitHub URL of the project's codebase

## SETUP INFO

1. git clone GitHub URL
2. cd HNG12_Backend
3. cd Task_0
4. run uvicorn main:app --reload

## API DOCS

Endpoint: /stats
Method: GET
Response Format: json object

## Example Usage

curl 
curl -X GET "http://100.25.191.235:8000/stats" -H "accept: application/json"

python
import requests

url = "http://100.25.191.235:8000/stats"
response = requests.get(url)
print(response.json())

## Backlink

1. https://hng.tech/hire/python-developers
