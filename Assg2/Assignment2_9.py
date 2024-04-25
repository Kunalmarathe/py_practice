
def lengthOfNumber(No):
    
    if(No > 9):
        return len(str(No))
    elif(No < 0):
        return len(str(No)) - 1
    else:
        return 1

def main():
    print("Enter a number : ")
    No = int(input())

    Result = lengthOfNumber(No)

    print("The length of the number is : ",Result)

if __name__ == "__main__":
    main()