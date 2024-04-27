
def CheckEven(A):
    return (A%2 == 0)

CheckEvenX = lambda A : (A%2 == 0)

def main():
    Ret = CheckEvenX(10)
    if(Ret == True):
        print("Its even number")
    else:
        print("Its odd number")

if __name__ == "__main__":
    main()