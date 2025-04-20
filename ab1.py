from celery.result import AsyncResult
from tasks import app

task_id = '8ef20756-545f-453b-990f-e9a5e010b45c'
res = AsyncResult(task_id, app=app)
print(res.state)  # Should not throw error
