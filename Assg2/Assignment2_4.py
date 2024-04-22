
def addOfFactor(No):
    sum = 0
    i = 1
    while(i < No):
        if(No % i == 0):
            sum = sum + i
        i = i + 1

    return sum

def main():
    print("Enter the number : ")
    No = int(input())

    Result = addOfFactor(No)

    print("The factor of ",No,"is : ",Result)

if __name__ == "__main__":
    main()