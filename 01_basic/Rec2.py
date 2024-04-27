# here it just print the limt that we given that is 1500. but in reality
# it's given to us. At the time of runtime it generates the error 

import sys

def main():
    print("Recursion limit is : ",sys.getrecursionlimit())
    sys.setrecursionlimit(1500)
    print("Recursion limit is : ",sys.getrecursionlimit())    

if __name__ == "__main__":
    main()