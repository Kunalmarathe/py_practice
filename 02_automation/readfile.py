import os

def main():
  print("Enter the name of file that you want to open for reading purpose : ")
  Fname = input()

  if os.path.exists(Fname):
    fobj = open(Fname, "r") # r for read
    print("File is succesfully opened in write mode")
  
    Data = fobj.read()

    print(Data)

    fobj.close() # here it closes the file which is opened
    
  else:
    print("Unable to open file as file is not present is the current directory")

if __name__ == "__main__":
  main()

