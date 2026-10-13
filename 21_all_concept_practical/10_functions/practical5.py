# Task:
    # 1. greet(name="Guest") naam ka function banao.
    # 2. Function ke andar Hello, {name}! print karo.
    # 3. Function ko pehle bina argument ke call karo.
    # 4. Phir "Prince" argument ke saath call karo.
# Expected output:
    # Hello, Guest!
    # Hello, Prince!

def greet(name = "Guest"):
    print(f"Hello, {name}!")

greet()
greet("Prince")