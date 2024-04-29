
def frequency(No, list):
    iCnt = 0

    for Num in list:
        if(Num == No):
            iCnt += 1

    return iCnt

def main():
    print("Number of elements : ")
    size = int(input())

    print("Input Elements : ")
    Numbers = []

    for i in range(size):
        Numbers.append(int(input()))

    print("Element to search : ")
    freq = int(input())

    Result = frequency(freq, Numbers)

    print("The frequency is : ",Result)

if __name__ == "__main__":
    main()