
def isPrime(No):
    if(No <= 1):
        return False

def main():
    print("Enter a number : ")
    iNo = int(input())

    isPrime(iNo)

if __name__ == "__main__":
    main()