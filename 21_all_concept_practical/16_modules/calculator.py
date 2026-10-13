def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def square(n):
    return n * n

if __name__ == "__main__":
    print("Calculator module directly run hua")
    print("Addition:", add(10, 5))