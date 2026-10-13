# Ek program banao jo:
# 1. List comprehension se even numbers ke squares ki list banaye.
# 2. Generator expression se even numbers ke squares generate kare.
# 3. List ka result print kare.
# 4. Generator par next() se pehle 3 values nikale.
# 5. Generator ke remaining values ko list() mein convert kare.
# 6. sum() se ek naye generator ke saare even squares ka total nikale.
# 7. type() se list aur generator ka type check kare.
# Expected output:
# Even squares list: [4, 16, 36, 64, 100]
# First three generator values: 4 16 36
# Remaining generator values: [64, 100]
# Sum of even squares: 220
# List type: <class 'list'>
# Generator type: <class 'generator'>

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# List comprehension
even_number_squares = [
    x * x for x in numbers if x % 2 == 0
]
print("Even squares list:", even_number_squares)

# Generator expression
even_squares_generator = (
    x * x for x in numbers if x % 2 == 0
)

print(
    "First three generator values:",
    next(even_squares_generator),
    next(even_squares_generator),
    next(even_squares_generator)
)

print(
    "Remaining generator values:",
    list(even_squares_generator)
)

# New generator for sum
new_generator = (x * x for x in numbers if x % 2 == 0)
print("Sum of even squares:", sum(new_generator))

print("List type:", type(even_number_squares))
print("Generator type:", type(even_squares_generator))

