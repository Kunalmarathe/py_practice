import datetime
import time
import schedule

def schedule_Minute():
  print("Schedular executes after each minute : ",datetime.datetime.now())

def main():
  print("Current time is ",datetime.datetime.now())

  schedule.every(1).minute.do(schedule_Minute)

  while True:
    schedule.run_pending()
    time.sleep(1)


if __name__ == "__main__":
  main()