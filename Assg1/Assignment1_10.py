
def displayLen(name):
    if isinstance(name, str):
        print(len(name)) 
    else:
        print("Invalid input")

def main():
    
    print("Enter a name : ")
    
    displayLen(input())

if __name__ == "__main__":
    main()