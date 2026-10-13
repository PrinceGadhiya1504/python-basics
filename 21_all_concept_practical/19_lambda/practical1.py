# 1. lambda se ek number ka square calculate karo.
# 2. Do numbers ka sum calculate karo.
# 3. Teen numbers me se maximum number find karo.
# 4. Default argument ke saath multiplication calculate karo.
# 5. Ek number even hai ya odd, ye check karo.
# Test values:
# - Square: 5
# - Sum: 10, 20
# - Maximum: 10, 25, 15
# - Multiplication: 5 aur default multiplier 2
# - Even/odd: 8 aur 7
# Expected output:
# Square: 25
# Sum: 30
# Maximum: 25
# Multiplication: 10
# 8 is even: True
# 7 is even: False

square = lambda x : x * x
add = lambda x, y : x + y
maximum = lambda x, y, z : max(x, y, z)
# maximum = lambda x, y, z : (x if x > y else y) if (x if x > y else y) > z else z
multiplication = lambda x , y = 2 : x * y
even = lambda x : True if x % 2 == 0 else False

print("Square:", square(5))
print("Sum:", add(10, 20))
print("Maximum:", maximum(25, 10, 30))
print("Multiplication:", multiplication(5))
print("8 is even:", even(8))
print("7 is even:", even(7))