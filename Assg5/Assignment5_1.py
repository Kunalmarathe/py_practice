
i = 0

def Display():
    global i

    if(i > 0):
        print('*', end = "   " )
        i = i - 1
        Display()

def main():

    global i
    print("Input value : ")
    i = int(input())
    
    print("Output value : ")
    Display()
    

if __name__ == "__main__":
    main()