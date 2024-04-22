
def display(No):
    if(No < 1):
        print("Enter the positive value greater than 0")
        return
    
    while(No > 0):
        print("*",end = " ")
        No = No - 1

def main():
    
    print("Please enter the value : ")

    display(int(input()))


if __name__ == "__main__":
    main()