# if we not give start then process will not start
# here , is place holder for remaining parameteres
# what is orphened process
# here if we give the () for the EvenDisplay/ OddDisplay then it will considerd as calling of 
# that function
import multiprocessing

def EvenDisplay(No):
    print("List of even numbers : ")
    start = 2
    for i in range(No):
        print(start)
        start += 2

def OddDisplay(No):
    print("List of odd numbers : ")
    start = 1
    for i in range(No):
        print(start)
        start += 2

def main():
    print("Enter number : ")
    Value = int(input())


    p1 = multiprocessing.Process(target= EvenDisplay, args= (Value,))
    p2 = multiprocessing.Process(target= OddDisplay, args= (Value,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("End of main process")
    
if __name__ == "__main__":
    main()

