# Task
# Initial list:
# numbers = [10, 20, 30, 40, 50]
# Is par ye operations karo, isi order mein:
# 1. append(60) karo.
# 2. insert(1, 15) karo.
# 3. remove(30) karo.
# 4. First three elements ki slicing karke print karo.
# 5. numbers.copy() se copied_numbers banao. Phir copy mein append(70) karo.
# 6. Original list se list comprehension ke through even numbers ki list banao.
# 7. Original aur copied lists dono print karo.

# Expected output:
# First three: [10, 15, 20]
# Even numbers: [10, 20, 40, 50, 60]
# Original: [10, 15, 20, 40, 50, 60]
# Copy: [10, 15, 20, 40, 50, 60, 70]

numbers = [10, 20, 30, 40, 50]

numbers.append(60)
numbers.insert(1, 15)
numbers.remove(30)
print(f"First three: {numbers[:3]}")

copied_numbers = numbers.copy()
copied_numbers.append(70)

even_numbers = [x for x in numbers if x % 2 == 0]

print(f"Even numbers: {even_numbers}")
print(f"Original: {numbers}")
print(f"Copy: {copied_numbers}")