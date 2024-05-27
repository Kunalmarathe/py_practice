import os
import threading

def evenList(list):
  sum = 0
  for element in list:
    if element % 2 == 0:
      sum += element
  print("The addition of even numbers is : ",sum)

def oddList(list):
  sum = 0
  for element in list:
    if element % 2 != 0:
      sum += element
  print("The addition of odd numbers is : ",sum)

def main():
  print("Enter the count of numbers you want to enter : ")
  size = int(input())

  list = []
  print("Enter the numbers : ")

  for i in range(size):
    list.append(int(input()))

  p1 = threading.Thread(target= evenList, args= (list, ))

  p2 = threading.Thread(target= oddList, args= (list, ))

  p1.start()
  p1.join()

  p2.start()
  p2.join()

if __name__ == "__main__":
  main()