
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
    Result = addOfNum(int(input()))

    print("The addition of number is : ",Result)


if __name__ == "__main__":
    main()