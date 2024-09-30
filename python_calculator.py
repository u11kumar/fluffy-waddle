# Python Calculator

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Error: Division by zero!")
    return x / y

# Mapping operators to functions
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

operator = input("Enter an operator (+ - / *): ")
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

# Validate input
try:
    num1 = float(num1)
    num2 = float(num2)
except ValueError:
    print("Error: Invalid input! Please enter valid numbers.")
    exit()

# Perform calculation
if operator in operations:
    result = operations[operator](num1, num2)
    print(f"{num1} {operator} {num2} = {round(result)}")
else:
    print(f"Invalid Operation: {operator}")
