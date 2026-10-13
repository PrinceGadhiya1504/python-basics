# Task
    # 1. marks = 75 banao.
    # 2. Check karo ki marks 35 ya usse zyada hain.
    # 3. Check karo ki marks 100 ya usse kam hain.
    # 4. Dono conditions ko and se combine karo.
    # 5. not ka use karke final result ka opposite print karo.

# Expected output
    # Passed minimum marks: True
    # Within maximum marks: True
    # Valid marks: True
    # Invalid marks: False

marks = 75

min_marks = 35
max_marks = 100

print(f"Passed minimum marks: {marks >= min_marks}")
print(f"Within maximum marks: {marks <= max_marks}")
print(f"Valid marks: {marks >= min_marks and marks <= max_marks}")
print(f"Invalid marks: {not(marks >= min_marks and marks <= max_marks)}")