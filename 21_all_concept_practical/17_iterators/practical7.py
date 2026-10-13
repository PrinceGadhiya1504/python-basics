# Ek program banao jo generator functions ka pipeline create kare:
# 1. even_numbers(numbers) — sirf even numbers yield kare.
# 2. squares(numbers) — har number ka square yield kare.
# 3. greater_than_20(numbers) — sirf 20 se bade numbers yield kare.
# 4. In generators ko chain karke final result nikalo.
# 5. Final result ko list() mein convert karke print karo.
# 6. sum() se final values ka total nikalo.

# Expected output:
# Final values: [36, 64, 100]
# Total: 200

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def even_numbers(numbers):
    for num in numbers:
        if num % 2 == 0:
            yield num

def squares(numbers):
    for num in numbers:
        yield num * num

def greater_than_20(numbers):
    for num in numbers:
        if num > 20:
            yield num


even_gen = even_numbers(numbers)
squares_gen = squares(even_gen)
greater_than_20_gen = greater_than_20(squares_gen)

final_values = list(greater_than_20_gen)
print("Final values:", final_values)
print("Total:", sum(final_values))

# Generator expressions
even_gen_expr = (num for num in numbers if num % 2 == 0)
squares_gen_expr = (num * num for num in even_gen_expr)
greater_than_20_gen_expr = (num for num in squares_gen_expr if num > 20)

final_values_expr = list(greater_than_20_gen_expr)
print("Final values (expressions):", final_values_expr)
print("Total (expressions):", sum(final_values_expr))