# Name = lambda Parameters : Logic
# Name (_, _, ....)

def Addition(A, B):
    Ans = 0
    Ans = A + B
    return Ans

Add = lambda A,B : A + B 
cube = lambda A : A*A*A

def main():
    Ret = Add(10, 11)
    print("Addition is : ", Ret)

    cube = 2
    print("Cube is : ", cube)

if __name__ == "__main__":
    main()