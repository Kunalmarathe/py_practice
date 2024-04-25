
def isPrime(No):
    if(No <= 1):
        return False
        exit()
    
    for i in range(2, No):
        if(No % i == 0):
            return False
        
    return True


def main():
    print("Enter a number : ")
    iNo = int(input())

    Result = isPrime(iNo)

    if(Result == True):
        print("It is prime number")
    else:
        print("It is not prime number")

if __name__ == "__main__":
    main()