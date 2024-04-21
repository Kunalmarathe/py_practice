import sys

def main():
    print("Demostration of command line argument")
    print("Name of application : ",sys.argv[0])
    print("Datatype of argv is : ",type(sys.argv))
    print("Number of command line argument are : ",len(sys.argv))

if __name__ == "__main__":
    main()