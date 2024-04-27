# return is block specific word and there is no block in lambda so no return word
def CheckEven(A):
    return (A%2 == 0)

CheckEvenX = lambda A : (A%2 == 0)
# design pattern : it is pattern 
# here CheckEvenX is object of python. It is pure oop language. Also it have class for every function.
# General purpose language

def main():
    Ret = CheckEvenX(11)
    if(Ret == True):
        print("Its even number")
    else:
        print("Its odd number")

if __name__ == "__main__":
    main()