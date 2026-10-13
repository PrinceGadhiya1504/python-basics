# Apne folder 16_modules mein ek files banao.

# calculator.py

# Is file mein 4 functions banao:
# - add(a, b) — addition return kare.
# - subtract(a, b) — subtraction return kare.
# - multiply(a, b) — multiplication return kare.
# - divide(a, b) — division return kare; agar b == 0 ho, to "Cannot divide by zero" return kare.

# ------------------------
  
#  Present (Current) file mein:
# 1. calculator module import karo.
# 2. add() ko 10, 5 ke saath call karo.
# 3. subtract() ko 10, 5 ke saath call karo.
# 4. multiply() ko 10, 5 ke saath call karo.
# 5. divide() ko 10, 5 aur 10, 0 ke saath call karo.
# 6. Saare results print karo.

# Expected output
# Addition: 15
# Subtraction: 5
# Multiplication: 50
# Division: 2.0
# Division: Cannot divide by zero

import calculator

print("Addition:", calculator.add(10, 5))
print("Subtraction:", calculator.subtract(10, 5))
print("Multiplication:", calculator.multiply(10, 5))
print("Division:", calculator.divide(10, 5))
print("Division:", calculator.divide(10, 0))

