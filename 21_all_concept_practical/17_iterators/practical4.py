# Ek generator function square_generator(numbers) banao jo:
# 1. for loop se har number par iterate kare.
# 2. Har number ka square yield kare.
# 3. Generator object ko variable mein store karo.
# 4. next() se pehle do squares nikalo.
# 5. list() se remaining squares ki list banao.
# 6. Ek naye generator ko for loop se poora iterate karke print karo.
# Expected output
# First square: 4
# Second square: 16
# Remaining squares: [36, 64, 100]
# All squares:
# 4
# 16
# 36
# 64
# 100

numbers = [2, 4, 6, 8, 10]

def square_generator(numbers):
    for number in numbers:
        yield number * number
    
square = square_generator(numbers)

print("First square:", next(square))
print("Second square:", next(square))
print("Remaining squares:", list(square))

print("All squares:")
for number in square_generator(numbers):
    print(number)