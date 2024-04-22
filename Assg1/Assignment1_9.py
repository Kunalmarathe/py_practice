
def displayEvenNumber(No):

    if(No <= 0):
        print("Please enter a greater value than 0")
        return

    start = 2

    while(No > 0):
        print(start,end = " ")
        start = start + 2
        No = No - 1

def main():
    print("Enter a number : ")
    displayEvenNumber(int(input()))
   
if __name__ == "__main__":
    main()