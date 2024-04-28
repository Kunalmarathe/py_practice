# also wer can use from MarvellousFMR import *

import MarvellousFMR as MFMR

def main():
    Data = []

    print("Enter no of elements : ")
    size = int(input())

    print("Enter the elements : ")
    iCnt = 0

    for iCnt in range(0, size):
        No = int(input())
        Data.append(No)
    
    print("Data from input list : ",Data)

    FData = list(MFMR.filterX(MFMR.CheckEven, Data))
    print("Data after filter activity : ",FData)

    MData = list(MFMR.mapX(MFMR.Increase, FData))
    print("Data after map activity : ",MData)

    RData = MFMR.reduceX(MFMR.Add, MData)
    print("Data after reduce activity is : ",RData)

if __name__ == "__main__":
    main()