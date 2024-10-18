
from celery import Celery

app = Celery('tasks', broker='pyamqp://guest@localhost//')

@app.task
def process_data(data):
    return sum(data)
