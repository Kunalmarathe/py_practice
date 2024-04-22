def ChkNo(No):
    if(No > 0):
        print("Positive Number")
    elif(No < 0):
        print("Negative Number")
    else:
        print("Zero")
    

def main():
    print("Enter the number : ")

    ChkNo(int(input()))
    
if __name__ == "__main__":
    main()