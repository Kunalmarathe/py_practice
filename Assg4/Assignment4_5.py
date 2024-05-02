
from functools import reduce

def prime(No):
    if(No <= 1):
        return False
        

    for i in range(2, No):
        if(No%i == 0):
            return False
    
    return True


def main():
    print("How many numbers you want to enter : ")
    size = int(input())

    print("Enter the numbers : ")
    Data = []
    
    for i in range(size):
        Data.append(int(input()))
        
    FData = list(filter(prime,Data))
    print("List after filter : ", FData)

    MData = list(map((lambda A : A*2), FData))
    print("List after map : ",MData)

    RData = reduce((lambda A, B : A + B), MData)
    print("Output of reduce : ", RData)

if __name__ == "__main__":
    main()