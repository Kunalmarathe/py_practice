import datetime
import time
import schedule

def Schedule_Second():
  print("Schedular executes after each second : ",datetime.datetime.now())

def Schedular_Minute():
  print("Schedular executes after each minute : ",datetime.datetime.now())

def Schedular_Hour():
  print("Schedular executes after each hour : ",datetime.datetime.now())

def Schedular_Sunday():
    print("Schedular executes after each Sunday : ",datetime.datetime.now())



def main():
  print(datetime.datetime.now())

  schedule.every(5).seconds.do(Schedule_Second)
  schedule.every(1).minutes.do(Schedular_Minute)
  schedule.every(1).hours.do(Schedular_Hour)
  schedule.every().sunday.do(Schedular_Sunday)

  while True:
    schedule.run_pending()
    time.sleep(1)


if __name__ == "__main__":
  main()