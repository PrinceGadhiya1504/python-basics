# Task
# Ek list banao: numbers = [12, 5, 8, 21, 4, 15, 10]
# Is list par ye operations perform karo:
# 1. map() — har number ka square nikalo.
# 2. filter() — sirf even numbers select karo.
# 3. filter() — sirf 10 se bade numbers select karo.
# 4. sorted() — numbers ko ascending order me sort karo.
# 5. sorted() + lambda — numbers ko unke last digit ke basis par sort karo.
# Expected output
# Squares: [144, 25, 64, 441, 16, 225, 100]
# Even numbers: [12, 8, 4, 10]
# Numbers greater than 10: [12, 21, 15]
# Ascending order: [4, 5, 8, 10, 12, 15, 21]
# Sorted by last digit: [10, 21, 12, 4, 15, 5, 8]

numbers = [12, 5, 8, 21, 4, 15, 10]

square = list(map(lambda x : x * x, numbers))
even = list(filter(lambda x : x % 2 == 0, numbers))
greater_10 = list(filter(lambda x : x > 10, numbers))
sorted_asc = sorted(numbers)
sorted_last_digit = sorted(numbers, key = lambda x : x % 10)

print("Square:", square)
print("Even numbers:", even)
print("Numbers greater than 10:", greater_10)
print("Ascending order:", sorted_asc)
print("Sorted by last digit:", sorted_last_digit)