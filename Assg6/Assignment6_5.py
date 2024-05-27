import os
import threading

def displayForward():
  for i in range(1, 51):
    print(i)

def displayBackward():
  for i in range(50, 0, -1):
    print(i)

def main():
  
  thread1 = threading.Thread(target= displayForward)
  thread2 = threading.Thread(target= displayBackward)

  thread1.start()
  thread1.join()

  thread2.start()
  thread2.join()

if __name__ == "__main__":
  main()