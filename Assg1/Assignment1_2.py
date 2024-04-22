
def ChkNum(No):
    if(No % 2 == 0):
        print("Even number")
    else:
        print("Odd number")

def main():
    print("Enter an number : ")
    ChkNum(int(input()))

if __name__ == "__main__":
    main()