
from functools import reduce

CheckEven = lambda No : No%2 == 0

Increase = lambda No : No + 1

Add = lambda A,B: A + B

# self written fucntion filterX, mapX, reduceX

def filterX(Task, Elements):
    Result = [] 

    for no in Elements:
        if(Task(no) == True):
            Result.append(no)

    return Result

def mapX(Task, Elements):
    Result = []

    for no in Elements:

        Result.append(Task(no))

    return Result

def reduceX(Task, Elements):
    Sum = 0

    for no in Elements:
        Sum = Task(sum, no)
        
    return Sum

def main():
    Data = []

    print("Enter no of elements : ")
    size = int(input())

    print("Enter the elements : ")
    iCnt = 0

    for iCnt in range(0, size):
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