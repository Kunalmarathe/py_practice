print("Demostration of Object Orientation")

##########################################################
class Arithematic:
    def __init__(self,Value1,Value2):  # Constructor # Behaviour
        self.No1 = Value1   # Characteristics
        self.No2 = Value2   # Characteristics

    def Addition(self): # Behaviour
        Ans = self.No1  + self.No2
        return Ans
    
    def Substraction(self): # Behaviour
        Ans = self.No1 - self.No2
        return Ans
########################################################

print("Enter first number : ")
A = int(input())

print("Enter second number : ")
B = int(input())

obj = Arithematic(A,B)

Ret = obj.Addition()
print("Additon is : ",Ret)

Ret = obj.Substraction()
print("Substraction is : ",Ret)