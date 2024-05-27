import os

def main():
  print("Enter the name of file that you want to create : ")
  Fname = input()

  if os.path.exists(Fname):
    fobj = open(Fname, "a") # a for append
    print("File is succesfully opened in write mode")
  
    print("Enter data that you want to write in the file")
    Data = input()

    fobj.write(Data)

    fobj.close() # here it closes the file which is opened
    
  else:
    print("Unable to open file as file is not present is the current directory")

if __name__ == "__main__":
  main()

