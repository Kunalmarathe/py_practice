
def addOfNum(No):
    if(No < 10):
        return No

    iAddition = 0

    while No:
        iTemp = No % 10
        iAddition = iAddition + iTemp
        No //= 10

    return iAddition


def main():
    print("Enter a number : ")
    iNo = int(input())

    if(iNo < 0):
        print("Please enter a number greater than 0")
        main()
    else:
        Result = addOfNum(iNo)
        print("The addition of number is : ",Result)

if __name__ == "__main__":
    main()