
def Add(No1, No2):
    return No1 + No2

def main():
    print("Enter first number : ")
    no1 = int(input())

    print("Enter second number : ")
    no2 = int(input())

    Result = Add(no1, no2)

    print("The addition is : ",Result)

if __name__ == "__main__":
    main()