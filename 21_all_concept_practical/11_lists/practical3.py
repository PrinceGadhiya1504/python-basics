# Task
# Student marks ki nested list banao:
# students = [
#     ["Amit", 80, 70, 90],
#     ["Neha", 60, 85, 75],
#     ["Raj", 30, 40, 35]
# ]

# Ab:
# 1. Nested loops ya suitable loop se har student ka naam aur marks print karo.
# 2. Har student ka total aur average calculate karo.
# 3. Har student ke liye Pass ya Fail print karo. Average 40 ya usse zyada ho to Pass.
# 4. Sabhi students ke averages ki list banao.
# 5. Averages ko descending order mein sort karke print karo.
# 6. List comprehension se sirf un students ke naam nikalo jinka average 60 ya usse zyada hai.

# Expected output:
# Amit: Total=240, Average=80.0, Status=Pass
# Neha: Total=220, Average=73.33333333333333, Status=Pass
# Raj: Total=105, Average=35.0, Status=Fail
# Sorted averages: [80.0, 73.33333333333333, 35.0]
# Students with average >= 60: ['Amit', 'Neha']

students = [
    ["Amit", 80, 70, 90],
    ["Neha", 60, 85, 75],
    ["Raj", 30, 40, 35]
]

for student in students:
    name = student[0]
    marks = student[1:]
    total = sum(marks)
    average = total / len(marks)
    if average >= 40:
        status = "Pass"
    else:
        status = "Fail"
    print(f"{name}: Total={total}, Average={average}, Status={status}")

averages = [sum(student[1:]) / len(student[1:]) for student in students]
print(f"Sorted averages: {sorted(averages, reverse=True)}")

students_avg_60_or_more = [student[0] for student in students if sum(student[1:]) / len(student[1:]) >= 60]
print(f"Students with average >= 60: {students_avg_60_or_more}")
