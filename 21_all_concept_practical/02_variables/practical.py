# Ek program banao jo:
    # 1. product_name variable mein product ka naam store kare.
    # 2. price variable mein product ki price store kare.
    # 3. quantity variable mein quantity store kare.
    # 4. In variables ki help se total bill calculate karke print kare.
    
# Expected output:
# Product: Keyboard
# Price: 500
# Quantity: 3
# Total Bill: 1500

# Rules: Abhi input(), loops aur functions use nahi karne. Sirf variables, numbers aur arithmetic operator use karo.

name = input("Enter product name: ")
price = int(input("Enter product price: "))
quantity = int(input("Enter product quantity: "))
total = price * quantity

print("Product:", name)
print("Price:", price)
print("Quantity:", quantity)
print("Total Bill:", total)
