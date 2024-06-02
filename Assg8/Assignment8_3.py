class Arithmatic:

  def __init__(self, value):
    self.Value = value

  def ChkPrime(self):
    if self.Value > 1:
      for i in range(2, self.Value):
        if (self.Value % i) == 0:
          return False
      return True
    else:
      return False
  
  def ChkPerfect(self):
    sum = 0

    for i in range(1, self.Value):
      if self.Value % i == 0:
        sum += i
    
    if(sum == self.Value):
      return True
    else:
      return False
    
  def Factors(self):
    factors = []
    if self.Value > 0:
      
      for i in range(1, self.Value):
        if self.Value % i == 0:
          factors.append(i)
      print("Factors are : ", factors)
    else:
      print("Invalid Number")

  def sumFactors(self):
    sum = 0
    if self.Value > 0:
      for i in range(1, self.Value):
        if self.Value % i == 0:
          sum += i
      
      print("The sum of factors is : ",sum)

    else:
      print("Invalid Number")

number = int(input("Enter the number : "))
obj1 = Arithmatic(number)

print(obj1.ChkPrime())
print(obj1.ChkPerfect())

number = int(input("Enter the number : "))

obj2 = Arithmatic(number)

obj2.Factors()
obj2.sumFactors()