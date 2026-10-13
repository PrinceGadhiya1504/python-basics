# calculator.py mein ye improvements karo:
# 1. Ek naya function square(n) banao jo number ka square return kare.
# 2. File ke end mein if __name__ == "__main__": use karke ek test print rakho. Ye test sirf tab chale jab calculator.py directly run ho.

# Phir this(practical3.py) file me:
# 1. from calculator import add, square use karke functions import karo.
# 2. calculator module ko calc alias se import karke bhi ek function call karo.
# 3. add(20, 30) ka result print karo.
# 4. square(6) ka result print karo.
# 5. calc.multiply(4, 5) ka result print karo.

# Expected output
# Addition: 50
# Square: 36
# Multiplication: 20

# Dhyan rahe: practical3.py run karne par calculator.py ka if __name__ == "__main__": wala test print nahi hona chahiye.

from calculator import add, square
import calculator as calc

print("Addition:", add(20, 30))
print("Square:", square(6))
print("Multiplication:", calc.multiply(4, 5))
