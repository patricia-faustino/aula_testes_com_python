def sum(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiply(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b