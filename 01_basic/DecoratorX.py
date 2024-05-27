
# predefined function
def sub(A, B):        # 0*100
  print(A - B)        

def SmartSub(fptr):       # 0*200
  def Inner(A,B):         # 0*300
    if A < B:
      A,B = B,A
    return fptr(A,B)
  return Inner            # 0*300

sub = SmartSub(sub)       # SmartSub(0*100)

def main():               # 0*400
  No1 = int(input("Enter first number : "))
  No2 = int(input("Enter second number : "))

  sub(No1, No2)           # 0*300(1990, 1992)


if __name__ == "__main__":
  main()