
def Minimum(Num):
    result = Num[0]

    for i in Num:
        if(i < result):
            result = i

    return result

def main():
    print("Enter how many numbers you want to add : ")
    length = int(input())

    print("Enter the numbers : ")
    Numbers = []

    for i in range(length):
        Numbers.append(int(input()))
        
    Result = Minimum(Numbers)

    print("The minimum is : ",Result)

if __name__ == "__main__":
    main()