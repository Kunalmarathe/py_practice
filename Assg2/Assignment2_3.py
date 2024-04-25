def factorial(No):
    sum = 1

    while(No > 0):
        sum = sum * No
        No = No - 1

    return sum

def main():
    print("Enter a number : ")
    No = int(input())

    if(No <= 0):
        print("Please enter a number greater than 0")
        main()
    else:
        Result = factorial(No)
        print("The factorial of ",No," is : ",Result)

if __name__ == "__main__":
    main()