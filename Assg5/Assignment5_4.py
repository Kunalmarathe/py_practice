
sum = 0

def summation(No):
    global sum

    if(No > 0):
        sum += No%10
        summation(int(No/10))

def main():

    print("Enter input value : ")
    value = int(input())

    summation(value)

    print("The summation is : ",sum)

if __name__ == "__main__":
    main()