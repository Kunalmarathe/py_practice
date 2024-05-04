# give input of 100
# here output get's mixed
# here added even and odd to chek zig zag output
# thread scheduling 
# time quantum
# don't do user interaction in threading
# command promant limitation : it print serially not parallay
# therading then processing > ligntweight then heavy weight

import threading

def EvenDisplay(No):
   
    print("List of even numbers : ")
    start = 2
    for i in range(No):
        print("Even : ",start)
        start += 2

def OddDisplay(No):
    
    print("List of odd numbers : ")
    start = 1
    for i in range(No):
        print("Odd : ",start)
        start += 2

def main():

    print("Enter number : ")
    Value = int(input())

    p1 = threading.Thread(target= EvenDisplay, args= Value)
    p2 = threading.Thread(target= OddDisplay, args= Value)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("End of main process")
    
if __name__ == "__main__":
    main()

