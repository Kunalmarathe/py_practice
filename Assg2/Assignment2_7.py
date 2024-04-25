
def patternPrinting(No):
    for i in range(No):
        print()
        for j in range(No):
            print(j+1, end = "  ")


def main():
    print("Enter a number : ")
    patternPrinting(int(input()))

if __name__ ==  "__main__":
    main()