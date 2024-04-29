
def addition(Num):
    sum = 0
    
    for no in Num:
        sum += no

    return sum

def main():
    print("Number of elements : ")
    size = int(input())

    Numbers = []

    for i in range(size):
        Numbers.append(int(input()))
        

    Result = addition(Numbers)

    print("The addition is : ",Result)

if __name__ == "__main__":
    main()