# Task: Simple calculator
    # 1. a = 10 banao.
    # 2. b = 5 banao.
    # 3. operator = "*" banao.
    # 4. match statement se operator check karo:
    #    - "+" ho to addition.
    #    - "-" ho to subtraction.
    #    - "*" ho to multiplication.
    #    - "/" ho to division.
    #    - Kisi aur operator ke liye "Invalid operator" print karo.
# Expected output:
    # Result: 50

a = 10
b = 5
operator = "*"

match operator:
    case "+":
        print(f"Result: {a + b}")
    case "-":
        print(f"Result: {a - b}")
    case "*":
        print(f"Result: {a * b}")
    case "/":
        print(f"Result: {a / b}")
    case _:
        print("Invalid operator")