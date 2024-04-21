def main():
    print("Enter no of ele that you want to insert : ")
    size = int(input())

    Arr = list()

    print("Enter the elements : ")

    for i in range(size):
        no = int(input())
        Arr.append(no)

    print("Entered elemensts : ", Arr)

if __name__ == "__main__":
    main()