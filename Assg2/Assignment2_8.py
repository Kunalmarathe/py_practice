
def patternPrinting(No):
    start = 1
    while(start <= No):
        for i in range(start):
            print(i+1, end = " ")
        print()
        start = start + 1


def main():
    print("Enter a number : ")
    patternPrinting(int(input()))

if __name__ == "__main__":
    main()