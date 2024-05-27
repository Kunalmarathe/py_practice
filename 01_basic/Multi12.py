# multicore
import multiprocessing
import os
import time

def Fun(No):
    Sum = 0
    print("PID is : ",os.getpid())
    for i in range(No):
        Sum = Sum + (No**3)
    return Sum


def main():
    
    starttime = time.time()
    Arr = [100000,200000,300000,400000,500000, 600000, 700000, 800000, 900000, 1000000]
    Result = []

    p = multiprocessing.Pool()
    Result = p.map(Fun,Arr)
    p.close()
    p.join()

    print(Result)
    endtime = time.time()
    print("Time required for execution : ",endtime-starttime)

if __name__ == "__main__":
    main()