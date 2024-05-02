Start = 1
End = 1

def Display():
    global Start

    if(Start <= End):
        print(Start)
        Start += 1
        Display()
   

def main():

    global End
    print("Enter input value : ")
    End = int(input())

    print("Output : ")
    Display()


if __name__ == "__main__":
    main()