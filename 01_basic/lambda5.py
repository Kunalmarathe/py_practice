
def CheckEven(A):
    if(A%2 == 0):
        return True
    else:
        return False
    
# evenOdd = lambda A : if(A % 2 == 0): return 1 else: return 0

def main():
    Ret = CheckEven(10)
    if(Ret == True):
        print("Its even number")
    else:
        print("Its odd number")

if __name__ == "__main__":
    main()