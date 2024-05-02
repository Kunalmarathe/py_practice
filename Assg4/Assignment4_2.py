
power = lambda A, B  : A * B

def main():
    print("Enter the first number : ")
    No1 = int(input())

    print("Enter the second number : ")
    No2 = int(input())
    
    Result = power(No1, No2)

    print("The multiplication is : ",Result)


if __name__ == "__main__":
    main()