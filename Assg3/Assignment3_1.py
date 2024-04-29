def addition(Num):
    sum = 0
    
    for no in Num:
        sum += no

    return sum

def main():
    print("Enter how many numbers you want to add : ")
    length = int(input())

    Numbers = []

    for i in range(length):
        Numbers.append(int(input()))
        i += 1

    Result = addition(Numbers)

    print("The addition is : ",Result)

if __name__ == "__main__":
    main()