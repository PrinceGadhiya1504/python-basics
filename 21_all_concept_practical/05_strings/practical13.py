# String formatting with f-strings
# Task
    # 1. product = "Keyboard" banao.
    # 2. price = 750 banao.
    # 3. quantity = 2 banao.
    # 4. F-string ki help se product name, price aur quantity print karo.
    # 5. F-string ke andar calculation karke total bill bhi print karo.
# Expected output:
    # Product: Keyboard
    # Price: 750
    # Quantity: 2
    # Total Bill: 1500

product = "Keyboard"
price = 750
quantity = 2

print(f"Product: {product}")
print(f"Price: {price}")
print(f"Quantity: {quantity}")
print(f"Total Bill: {price * quantity}")