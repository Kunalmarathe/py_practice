# Name = lambda Parameters : Logic
# Name (_, _, ....)

def Cube(A):
    return A*A*A

#we can use A**3 it's only in py
    
CubeX = lambda A : A*A*A

def main():
    Ret = CubeX(10, 11)
    print("Addition is : ", Ret)

    cube = 2
    print("Cube is : ", cube)

if __name__ == "__main__":
    main()