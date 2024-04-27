# factorial of the given value

i = 1
Fact = 1

def Factorial(No):
    global i
    global Fact

    if(No >= 1):
        Fact = Fact * No
        No = No - 1
        Factorial(No)

    return Fact

def main():

    print("Enter a number : ")
    Value = int(input())
    
    Result = Factorial(Value)

    print("Factorial is : ",Result)

if __name__ == "__main__":
    main()