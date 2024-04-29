
import MarvellousNum

Add = lambda A,B : A + B

def ListPrime():
    print("Number of elements : ")
    size = int(input())

    print("Input Elements : ")
    Number = []

    for i in range(size):
        Number.append(int(input()))
       
    sum = 0

    for No in Number:
        if(MarvellousNum.ChkPrime(No) == True):
            sum = Add(sum, No)        
    
    print("The addition is : ",sum)

if __name__ == "__main__":
    ListPrime()