
def Minimum(Num):
    result = Num[0]

    for i in Num:
        if(i < result):
            result = i

    return result

def main():
    print("Number of elements : ")
    size = int(input())

    print("Input Elements : ")
    Numbers = []

    for i in range(size):
        Numbers.append(int(input()))
        
    Result = Minimum(Numbers)

    print("The minimum is : ",Result)

if __name__ == "__main__":
    main()