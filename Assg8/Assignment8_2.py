class BankAccount:
  ROI = 10.5

  def __init__(self, name, amount):
    self.Name = name
    self.Amount = amount

  def Desposit(self):
    amount = int(input("Enter the amount: "))
    self.Amount += amount

  def Withdraw(self):
    amount = int(input("Enter the amount to be withdraw: "))
    self.Amount -= amount

  def CalculateIntrest(self):
    print("The intrest is: ", ((self.Amount/100) * BankAccount.ROI))

  def Display(self):
    print("The name is: ",self.Name)
    print("The amount is: ",self.Amount)

userName = input("Enter the name: ")
userAmount = int(input("Enter the amount: "))

obj1 = BankAccount(userName, userAmount)

obj1.Display()

obj1.Withdraw()
obj1.Display()

obj1.Desposit()
obj1.CalculateIntrest()

obj1.Display()