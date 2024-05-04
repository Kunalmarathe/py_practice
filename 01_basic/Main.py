def even(No):
    start = 2
    for i in range(No):
        if(start <= No ):
            print(start)
            start += 2

def odd(No):
    start = 1
    for i in range(No):
        if(start <= No):
            print(start)
            start += 2

def main():
    even(20)
    odd(20)

if __name__ == "__main__":
    main()

