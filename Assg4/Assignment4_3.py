
from functools import reduce

def main():
    print("How many numbers you want to enter : ")
    size = int(input())

    Data = []
    print("Enter the numbers : ")

    for i in range(size):
        Data.append(int(input()))

    print("Input List : ",Data)

    FData = list(filter((lambda No : 70 <= No <= 90), Data))
    print("List after filter : ",FData)

    MData = list(map((lambda No : No + 10), FData))
    print("List after map : ",MData)

    RData = reduce((lambda A, B : A + B), MData)
    print("Output of reduce : ",RData)


if __name__ == "__main__":
    main()