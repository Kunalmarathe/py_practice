def printPattern(No):
    for i in range(No):
        print()
        for j in range(No):
            print('*', end = "  ")

def main():
    print("Enter a numeric value : ")
    No = int(input())

    printPattern(No)

if __name__ == "__main__":
    main()