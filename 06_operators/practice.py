# 1. Arithmetic Operators
# Arithmetic operators are used with numeric values to perform common mathematical operations:
    # + : Addition
    # - : Subtraction
    # * : Multiplication
    # / : Division
    # % : Modulus
    # ** : Exponentiation
    # // : Floor Division

a = 15
b= 4

print("Arithmetic a+b: ", a + b)
print("Arithmetic a-b: ", a - b)
print("Arithmetic a*b: ", a * b)
print("Arithmetic a/b: ", a / b)
print("Arithmetic a%b: ", a % b)
print("Arithmetic a**b: ", a ** b)
print("Arithmetic a//b: ", a // b)

# 2. Assignment Operators
# Assignment operators are used to assign values to variables:
    # = : Assignment
    # += : Addition Assignment
    # -= : Subtraction Assignment
    # *= : Multiplication Assignment
    # /= : Division Assignment
    # %= : Modulus Assignment
    # **= : Exponentiation Assignment
    # //= : Floor Division Assignment

a = 15
b = 4

# Demonstrating assignment operations (resetting a = 15 each time for clarity)
a = b
print("Assignment a=b: ", a)

a = 15
a += b
print("Assignment a+=b: ", a)

a = 15
a -= b
print("Assignment a-=b: ", a)

a = 15
a *= b
print("Assignment a*=b: ", a)

a = 15
a /= b
print("Assignment a/=b: ", a)

a = 15
a %= b
print("Assignment a%=b: ", a)

a = 15
a **= b
print("Assignment a**=b: ", a)

a = 15
a //= b
print("Assignment a//=b: ", a)

# 3. Comparison Operators
# Comparison operators are used to compare values:
    # == : Equal to
    # != : Not equal to
    # > : Greater than
    # < : Less than
    # >= : Greater than or equal to
    # <= : Less than or equal to

a = 15
b = 4

print("Comparison a==b: ", a == b)
print("Comparison a!=b: ", a != b)
print("Comparison a>b: ", a > b)
print("Comparison a<b: ", a < b)
print("Comparison a>=b: ", a >= b)
print("Comparison a<=b: ", a <= b)

# 4. Logical Operators
# Logical operators are used to perform logical operations:
    # and : Logical AND
    # or : Logical OR
    # not : Logical NOT

a = 15

print("Logical a > 0 and a < 10: ", a > 0 and a < 10)
print("Logical a > 0 or a < 10: ", a > 0 or a < 10)
print("Logical not a > 0: ", not a > 0)


# 5. Identity Operators
# Identity operators are used to compare the memory locations of objects:
    # is : True if both variables are the same object
    # is not : True if both variables are not the same object

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

# is - Checks if both variables point to the same object in memory
# == - Checks if the values of both variables are equal
print("Identity x is z: ", x is z) # True - kyuki x and z same object hai
print("Identity x is y: ", x is y) # False - kyuki x and y alag alag objects hain
print("Identity x == y: ", x == y) # True - kyuki dono me same values hai
print("Identity x is not y: ", x is not y) # True - kyuki x and y alag alag objects hain


# 6. Membership Operators
# Membership operators are used to check if a value is present in a sequence:
    # in : True if the value is present in the sequence
    # not in : True if the value is not present in the sequence

fruits = ["apple", "banana", "cherry"]

print("Membership banana in fruits: ", "banana" in fruits)
print("Membership pineapple not in fruits: ", "pineapple" not in fruits)

text = "Hello World"

print("Membership H in text: ", "H" in text)
print("Membership Hello in text: ", "Hello" in text)
print("Membership hello in text: ", "hello" in text)
print("Membership z not in text: ", "z" not in text)


# 7. Bitwise Operators
# Bitwise operators are used to perform operations on binary numbers:
    # & : Bitwise AND
    # | : Bitwise OR
    # ^ : Bitwise XOR
    # ~ : Bitwise NOT
    # << : Left Shift
    # >> : Right Shift

a = 15
b = 4

#binary representation use kar rahe hain
# 15 = 1111
#  4 = 0100

# 1 & 1 = 1
# 1 & 0 = 0
# 0 & 1 = 0
# 0 & 0 = 0

# AND
#  1111
#  0100
#  -----
#  0100

print("Bitwise a & b: ", a & b)

#OR
# 1 | 1 = 1
# 1 | 0 = 1
# 0 | 1 = 1
# 0 | 0 = 0
#  1111
#  0100
#  -----
#  1111

print("Bitwise a | b: ", a | b)

#XOR
# 0 ^ 0 = 0
# 0 ^ 1 = 1
# 1 ^ 0 = 1
# 1 ^ 1 = 0
#  1111
#  0100
#  -----
#  1011
print("Bitwise a ^ b: ", a ^ b)

#NOT
# ~ ek number ke bits ko invert karta hai
# 0 → 1
# 1 → 0
# 15 = 1111
# ~15 = 0000
# Python integers ke liye bitwise operations two's-complement representation ke equivalent behavior 
# follow karte hain. Isliye useful mathematical rule hai:
# ~x = -(x+1)

# ~15
# = -(15 + 1)
# = -16

print("Bitwise ~a: ", ~a)


#Left Shift
# Left Shift - Bits ko left side shift karta hai
# 15 = 00001111
# << 2
# 00111100 → 60
print("Bitwise a << b: ", a << b)

#Right Shift
# Right Shift - Bits ko right side shift karta hai
# 15 = 00001111
# >> 2
# 00000011 → 3
print("Bitwise a >> b: ", a >> b)