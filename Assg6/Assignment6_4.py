import os
import threading

def small(Value):
  print("The id of thread is : ", os.getpid())
  print("The name of thread is small")

  sum = 0
  for ch in Value:  
    if 'a' <= ch <= 'z':
      sum += 1
  print("The total number of small character is : ",sum)

def capital(Value):
  print("The id of thread is : ", os.getpid())
  print("The name of thread is capital")

  sum = 0
  for ch in Value:
    if 'A' <= ch <= 'Z':
      sum += 1
  print("The total number of capital character is : ",sum)

def digits(Value):
  print("The id of thread is : ", os.getpid())
  print("The name of thread is digits")

  sum = 0
  for ch in Value:
    if '0' <= ch <= '9':
      sum += 1
  print("The total number of digits is : ",sum)

def main():
  print("Enter the value : ")
  Value = input()

  p1 = threading.Thread(target= small, args= (Value, ))
  p2 = threading.Thread(target= capital, args= (Value, ))
  p3 = threading.Thread(target= digits, args= (Value, ))

  p1.start()
  p1.join()

  p2.start()
  p2.join()

  p3.start()
  p3.join()

  print("Exit from main")

if __name__ == "__main__":
  main()