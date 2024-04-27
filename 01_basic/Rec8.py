# to print a value in reverse order

i = 1

def DisplayR(No):
    global i

    if(No >= i):
        print(No)
        No = No - 1
        DisplayR(No)

def main():
    print("Enter a number : ")
    Value = int(input())
    DisplayR(Value)

if __name__ == "__main__":
    main()