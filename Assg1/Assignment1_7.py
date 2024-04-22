
def divBy5(No):
    if(No % 5 == 0):
        print("True")
    else:
        print("False")

def main():

    print("Enter a positive value : ")
    
    divBy5(int(input()))

if __name__ == "__main__":
    main()