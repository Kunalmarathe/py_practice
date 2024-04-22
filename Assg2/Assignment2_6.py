
def printPattern(No):
    for i in range(No):
        print()
        for j in range(No - i):
            print('*',end = " ")

def main():
    print("Enter a number : ")
    iNo = int(input())

    printPattern(iNo)

if __name__ == "__main__":
    main()

