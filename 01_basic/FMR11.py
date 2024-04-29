

from MarvellousFMR import *

CheckEven = lambda No : (No % 2 == 0)
Increase = lambda No : No + 1
Add = lambda A, B : A + B

def main():
    Data = []

    print("Enter no of elements : ")
    size = int(input())

    print("Enter the elements : ")

    for i in range(0, size):
        No = int(input())
        Data.append(No)
    
    print("Data from input list : ",Data)

    FData = list(filterX(CheckEven, Data))
    print("Data after filter activity : ",FData)

    MData = list(mapX(Increase, FData))
    print("Data after map activity : ",MData)

    RData = reduceX(Add, MData)
    print("Data after reduce activity is : ",RData)

if __name__ == "__main__":
    main()