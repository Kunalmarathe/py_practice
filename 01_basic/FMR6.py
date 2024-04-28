from functools import reduce

CheckEven = lambda No : No%2 == 0

Increase = lambda No : No + 1

Add = lambda A,B: A + B

# self written fucntion

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



def main():
    Data = [11, 14, 20, 23, 18, 16, 15, 20]
    print("Data from input list : ",Data)

    FData = list(filterX(CheckEven, Data))
    print("Data after filter activity : ",FData)

    MData = list(mapX(Increase, FData))
    print("Data after map activity : ",MData)

    RData = reduce(Add, MData)
    print("Data after reduce activity is : ",RData)

if __name__ == "__main__":
    main()