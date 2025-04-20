from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from celery import Celery
from tasks import summarize_text

app = FastAPI()
cache = {}
class SummarizationRequest(BaseModel):
    text: str
async def summarize(request: SummarizationRequest):
    if request.text in cache:
        return {"summary": cache[request.text]}
    
    task = summarize_text.delay(request.text)
    return {"task_id": task.id}
async def get_result(task_id: str):
    task = summarize_text.AsyncResult(task_id)
    if task.state == 'PENDING':
        return {"status": "Pending"}
    elif task.state == 'SUCCESS':
        return {"status": "Success", "summary": task.result}
    else:
        return {"status": "Failed"}
