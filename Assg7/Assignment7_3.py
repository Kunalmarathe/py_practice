class Arithematic:
  def __init__(self):
    self.Value1 = 0
    self.Value2 = 0

  def Accept(self):
    self.Value1 = int(input("Enter the first number : "))
    self.Value2 = int(input("Enter the second number : "))

  def Addition(self):
    result = self.Value1 + self.Value2
    print("The addition is : ",result)

  def Substraction(self):
    result = self.Value1 - self.Value2
    print("The substraction is : ",result)

  def Multiplication(self):
    result = self.Value1 * self.Value2
    print("The multiplication is : ",result)

  def Devision(self):
    result = self.Value1 / self.Value2
    print("The devisio is : ",result)

obj1 = Arithematic()

obj1.Accept()
obj1.Addition()
obj1.Substraction()
obj1.Multiplication()
obj1.Devision()

obj2 = Arithematic()

obj2.Accept()
obj2.Addition()
obj2.Substraction()
obj2.Multiplication()
obj2.Devision()
