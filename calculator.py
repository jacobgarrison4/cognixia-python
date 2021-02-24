num1 = int(input("Enter first number: \n"))
num2 = int(input("Enter second number: \n"))

def add(x, y):
    return (x + y)

print(add(num1, num2))

def subtract(x, y):
    return x - y
    
print(subtract(num1, num2))

def multiply(x, y):
    return x * y

print(multiply(num1, num2))

def divide(x, y):
    return x / y

print(divide(num1, num2))

def square(x):
    return x ** 2

print(square(num1))
print(square(num2))