
import schedule
import time

def run_scheduled_task(task_name):
    print(f"Running scheduled task: {task_name}")

schedule.every(1).minutes.do(run_scheduled_task, task_name="data_sync")

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(1)
