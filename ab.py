# from celery import Celery
# app = Celery(
#     'tasks',
#     broker='redis://localhost:6379/0',
#     backend='redis://localhost:6379/0'
# )
import redis

r = redis.Redis(host='localhost', port=6379)
print(r.ping())  # Should print True
