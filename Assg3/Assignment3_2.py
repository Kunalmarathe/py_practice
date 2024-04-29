
def Maximum(Num):
    result = 0

    for i in Num:
        if(result < i):
            result = i

    return result

def main():
    print("Number of elements : ")
    size = int(input())
    
    print("Input Elements : ")
    Numbers = []

    for i in range(size):
        Numbers.append(int(input()))

    Result = Maximum(Numbers)

    print("The maximum number is : ",Result)

if __name__ == "__main__":
    main()