from functools import reduce

# CheckEven = lambda No : No%2 == 0
# Increase = lambda No : No + 1
# Add = lambda A,B: A + B

def main():
    Data = [11, 14, 20, 23, 18, 16, 15, 20]
    print("Data from input list : ",Data)

    FData = list(filter((lambda No : No%2 == 0), Data))
    print("Data after filter activity : ",FData)

    MData = list(map((lambda No : No + 1), FData))
    print("Data after map activity : ",MData)

    RData = reduce((lambda A,B: A + B), MData)
    print("Data after reduce activity is : ",RData)

if __name__ == "__main__":
    main()