
def Maximum(Num):
    result = 0

    for i in Num:
        if(result < i):
            result = i

    return result

def main():
    print("Enter how many numbers you want to add : ")
    length = int(input())

    Numbers = []

    for i in range(length):
        Numbers.append(int(input()))
        length -= 1

    Result = Maximum(Numbers)

    print("The maximum number is : ",Result)

if __name__ == "__main__":
    main()