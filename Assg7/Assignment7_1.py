class Demo:
  Value = 0

  def __init__(self, Value1, Value2):
    self.no1 = Value1
    self.no2 = Value2

  def Fun(self):
    print(self.no1, self.no2)

  def Gun(self):
    print(self.no1, self.no2)

  
print("Enter the first number : ")
val1 = int(input())

print("Enter the second number : ")
val2 = int(input())

obj1 = Demo(11, 21)
obj2 = Demo(51, 101)

obj1.Fun()
obj2.Fun()

obj1.Gun()
obj2.Gun()    
