#calculator
class calculator:
    def __init__(self):
        pass
    def add(self,num1,num2):
        return num1+num2
    def subtract(self,num1,num2):
        return num1-num2
    def multiply(self,num1,num2):
        return num1*num2
    def divide(self,num1,num2):
        if num2!=0:
            return num1/num2
        else:
            print("Error:Can not divide with zero")
calc = calculator()
print("Addition:", calc.add(2, 9))
print("Subtraction:", calc.subtract(8.1, 2.4))
print("Multiplication:", calc.multiply(4.5, 6.4))
print("Division:", calc.divide(10.2, 2.1))
