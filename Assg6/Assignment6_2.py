# threading program

import threading
import os

def EvenFactor(No):
  addition = 0
  for i in range (1, No + 1):
    if No % i == 0 and i % 2 == 0:
      addition += i
  print("The addition of even factors is ",addition)

def OddFactor(No):
  addition = 0
  for i in range (1, No + 1):
    if No % i == 0 and i % 2 != 0:
      addition += i
  print("The addition of odd factors is : ",addition)

def main():
  print("Enter a number : ")
  Value = int(input())

  p1 = threading.Thread(target= EvenFactor, args = (Value,))
  p2 = threading.Thread(target= OddFactor, args = (Value,))

  p1.start()
  p1.join()

  p2.start()
  p2.join()

  print("Exit from main")

if __name__ == "__main__":
  main()