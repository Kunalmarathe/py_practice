import os

def main():
  print("Enter the name of file that you want to open for reading purpose : ")
  Fname = input()

  if os.path.exists(Fname):
    fobj = open(Fname, "r") # r for read
    print("File is succesfully opened in read mode")

    str1 = fobj.readline()
    str2 = fobj.readline()
    str3 = fobj.readline()
    str4 = fobj.readline()

    print(str1)
    print(str2)
    print(str3)
    print(str4)

    fobj.close() # here it closes the file which is opened
    
  else:
    print("Unable to open file as file is not present is the current directory")

if __name__ == "__main__":
  main()

