import Arithmatic 

def main():
    print("Enter the first number : ")
    iNo1 = int(input())

    print("Enter the second number : ")
    iNo2 = int(input())

    Arithmatic.Add(iNo1, iNo2)
    Arithmatic.Div(iNo1, iNo2)
    Arithmatic.Mult(iNo1, iNo2)
    Arithmatic.Sub(iNo1, iNo2)

if __name__ == "__main__":
    main()