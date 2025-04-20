# tasks.py
from celery import Celery
import requests
from celery import Celery

app = Celery('tasks', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')

@app.task
def summarize_text(text):
    # Your logic here
    return text[:100]  # dummy example
# In-memory cache
cache = {}

GEMINI_API_URL = "https://api.gemini.com/summarize"
GEMINI_API_KEY = "GEMINI_API_KEY1"

@app.task
def summarize_text(text):
    if text in cache:
        return cache[text]

    headers = {
        "Authorization": f"Bearer {GEMINI_API_KEY1}",
        "Content-Type": "application/json"
    }

    response = requests.post(GEMINI_API_URL, json={"text": text}, headers=headers)
    
    if response.status_code == 200:
        summary = response.json().get("summary")
        cache[text] = summary
        return summary
    else:
        raise Exception(f"Gemini API failed: {response.status_code} - {response.text}")
