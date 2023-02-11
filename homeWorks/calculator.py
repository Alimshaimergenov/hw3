class Calculator:


    def __add__(self, num1, num2):
        return num1 + num2

    def __sub__(self, num1, num2):
        return num1 - num2

    def __mul__(self, num1, num2):
        return num1 * num2

    def __truediv__(self, num1, num2):
        return num1 / num2


cal = Calculator()

print(cal.__sub__(34, 23))
print(cal.__mul__(5, 32))
print(cal.__truediv__(34, 23))
print(cal.__add__(345, 54))