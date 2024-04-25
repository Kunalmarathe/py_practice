
def lengthOfNumber(No):
    if(No < 10 & No > 0):
        return 1

    length = 0
    while No:
        length += 1
        No //= 10
    
    return length

def main():
    print("Enter a number : ")
    No = int(input())
    Result = lengthOfNumber(No)

    print("The length of the number is : ",Result)

if __name__ == "__main__":
    main()