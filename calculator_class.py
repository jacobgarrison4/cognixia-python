import math
class Calculator():

    memory = None

    def __init__(self, brand):
        self.brand = brand
    
    def add(self, num1, num2):
        self.memory = num1 + num2
        return num1 + num2

    def subtract(self, num1, num2):
        self.memory = num1 - num2
        return num1 - num2

    def multiply(self, num1, num2):
        self.memory = num1 * num2
        return num1 * num2

    def divide(self, num1, num2):
        self.memory = num1 / num2
        return num1 / num2

    def square(self, num1):
        self.memory = num1 ** 2
        return num1 ** 2

    def square_root(self, num1):
        self.memory = math.sqrt(num1)
        return math.sqrt(num1)

    def last_ans(self):
        print(self.memory)

    def clear(self):
        self.memory = None

    def __str__(self):
        return self.brand

if __name__ == "__main_":
    my_calc = Calculator("Ti-83 Plus")
    print(my_calc)
    print(my_calc.add(4, 6))
    print(my_calc.subtract(4, 6))
    print(my_calc.multiply(4, 6))
    my_calc.last_ans()
    print(my_calc.divide(4, 6))
    print(my_calc.square(4))
    my_calc.clear()
    my_calc.last_ans()
    print(my_calc.square_root(4))

