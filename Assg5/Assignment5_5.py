
Fact = 1

def factorial(No):
    global Fact
    if(No > 0):
        Fact *= No
        factorial(No - 1)

def main():
    print("Enter a value : ")
    value = int(input())

    factorial(value)
    print("The factorial is : ",Fact)
if __name__ == "__main__":
    main()