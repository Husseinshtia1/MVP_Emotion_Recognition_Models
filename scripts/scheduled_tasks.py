
import schedule
import time

def job():
    print("Scheduled task executed.")

schedule.every(10).seconds.do(job)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(1)
