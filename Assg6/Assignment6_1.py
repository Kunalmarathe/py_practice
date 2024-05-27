# threading program 

import threading
import os

def EvenDiaplay(No):
  print("List of even numbers : ")
  x = 2
  for i in range(No):
    print(x)
    x += 2

def OddDisplay(No):
  print("List of odd numbers : ")
  x = 1
  for i in range(No):
    print(x)
    x += 2

def main(): 
  print("Enter a number : ")
  Value = int(input())

  p1 = threading.Thread(target = EvenDiaplay, args = (Value,))
  p2 = threading.Thread(target = OddDisplay, args= (Value,))

  p1.start()
  p1.join()

  p2.start()
  p2.join()

  print("Exit from main")

if __name__ == "__main__":
  main()