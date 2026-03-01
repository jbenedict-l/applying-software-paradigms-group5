def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b

def modulo(a, b):
    if b == 0:
        return "Error: Cannot modulo by zero!"
    return a % b

def calculate(num1, num2, operation):
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide,
        '%': modulo
    }
    
    if operation not in operations:
        return f"Error: '{operation}' is an invalid operation."
    
    return operations[operation](num1, num2)

# Usage Example:
result = calculate(10, 2, '/')
print(result)
