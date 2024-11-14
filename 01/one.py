# Q1) Simple Calculator : A basic program to add two numbers entered by the user

class Calculator:
    def __init__(self):
        pass

    def get_input(self):
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        return a, b

    def multiply(self):
        a, b = self.get_input()
        return f"Result of multiplication: {a * b}"
    
    def addition(self):
        a, b = self.get_input()
        return f"Result of addition: {a + b}"

    def subtract(self):
        a, b = self.get_input()
        return f"Result of subtraction: {a - b}"

    def divide(self):
        a, b = self.get_input()
        if b == 0:
            return "Error: Division by zero is not allowed."
        return f"Result of division: {a / b}"

    
calc = Calculator()

print("Addition : ",calc.addition())
print("Multiply : ",calc.multiply())
print("Substraction : ",calc.subtract())
print("Divide : ",calc.divide())
