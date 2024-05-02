Start = 1
End = 1

def Display():
    global Start
    if(Start >= End):
        print(Start, end ="  ")
        Start -= 1
        Display()

def main():
    global Start
    print("Enter input value : ")
    Start = int(input())

    print("Output : ")
    Display()

if __name__ == "__main__":
    main()
