

class Circle:
  PI = 3.14
  def __init__(self):
    self.Radius = 0.0
    self.Area = 0.0
    self.Circumference = 0.0

  def Accept(self):
    print("Enter the radius : ")
    self.Radius = int(input())

  def CalculateArea(self):
    self.Area = Circle.PI * self.Radius * self.Radius

  def CalculateCircumference(self):
    self.Circumference = 2 * Circle.PI * self.Radius

  def Display(self):
    print("The Radius is : ", self.Radius)
    print("The Area is : ", self.Area)
    print("The Circumference is : ", self.Circumference)

circle1 = Circle()

circle1.Accept()
circle1.CalculateArea()
circle1.CalculateCircumference()
circle1.Display()

circle2 = Circle()

circle2.Accept()
circle2.CalculateArea()
circle2.CalculateCircumference()
circle2.Display()