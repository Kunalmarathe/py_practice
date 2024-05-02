
from functools import reduce

def main():
    print("How many numbers you want to enter : ")
    size = int(input())
    
    print("Enter the numbers : ")
    Data = []
    
    for i in range(size):
        Data.append(int(input()))
    
    print("Input List : ",Data)

    FData = list(filter((lambda No : No % 2 == 0),Data))
    print("List after filter : ", FData)

    MData = list(map((lambda No : No * No), FData))
    print("List after map : ",MData)

    RData = reduce((lambda A, B : A + B), MData)
    print("Output of reduce : ", RData)

if __name__ == "__main__":
    main()