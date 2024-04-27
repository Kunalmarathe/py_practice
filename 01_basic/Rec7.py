# to print a value upto the given input starts from 1

i = 1

def DisplayR(No):
    global i

    if(i <= No):
        print(i)
        i = i + 1
        DisplayR(No)

def main():
    print("Enter a number : ")
    value = int(input())
    DisplayR(value)

if __name__ == "__main__":
    main()