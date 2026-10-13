# Task:
# 1. marks = [45, 78, 32, 90, 56, 78, 23] list banao.
# 2. List ka total aur average calculate karo.
# 3. Highest aur lowest marks find karo.
# 4. Sirf passing marks (40 ya usse zyada) ki new list banao.
# 5. Marks ko ascending order mein sort karke print karo.
# 6. 78 kitni baar aaya hai, count karo.
# 7. Original list ko print karke confirm karo ki sorting ke liye sorted() use karne se original list change nahi hui.

# Expected output:
# Total: 402
# Average: 57.42857142857143
# Highest: 90
# Lowest: 23
# Passing marks: [45, 78, 90, 56, 78]
# Sorted marks: [23, 32, 45, 56, 78, 78, 90]
# 78 count: 2
# Original marks: [45, 78, 32, 90, 56, 78, 23]

marks = [45, 78, 32, 90, 56, 78, 23]

total = sum(marks)
average = total / len(marks)
highest = max(marks)
lowest = min(marks)
passing_marks = list(filter(lambda x : x >= 40, marks))
sorted_marks = sorted(marks)
count_78 = marks.count(78)

print(f"Total: {total}")
print(f"Average: {average}")
print(f"Highest: {highest}")
print(f"Lowest: {lowest}")
print(f"passing marks: {passing_marks}")
print(f"sorted marks: {sorted_marks}")
print(f"78 count: {count_78}")
print(f"Original marks: {marks}")
