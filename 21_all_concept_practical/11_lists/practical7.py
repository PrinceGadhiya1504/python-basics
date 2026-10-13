# Ek function analyze_students(students) banao.
# 1. Agar list empty hai, toh "No students available" return karo.
# 2. Sabhi students ke marks ka average nikalo.
# 3. max() aur min() se highest aur lowest marks wale students nikalo.
# 4. sorted() aur lambda se students ko marks ke descending order mein sort karo.
# 5. List comprehension se 60 ya usse zyada marks wale students nikalo.
# 6. filter() se 60 se kam marks wale students nikalo.
# 7. Dictionary mein saare results return karo.
# 8. Normal list aur empty list, dono ko test karo.

# Expected result ke main points:
# - Average marks: 71.8
# - Highest: Neha, 92
# - Lowest: Raj, 45
# - Passing students: Amit, Neha, Priya
# - Below 60: Raj, Jay

students = [
    {"name": "Amit", "marks": 78},
    {"name": "Neha", "marks": 92},
    {"name": "Raj", "marks": 45},
    {"name": "Priya", "marks": 88},
    {"name": "Jay", "marks": 56}
]

def analyze_students(students):
    if not students:
        return "No students available"

    average = sum(student["marks"] for student in students) / len(students)
    highest = max(students, key=lambda x: x["marks"])
    lowest = min(students, key=lambda x: x["marks"])
    sorted_students = sorted(students, key=lambda x: x["marks"], reverse=True)
    passing_students = [student for student in students if student["marks"] >= 60]
    below_60 = [student for student in students if student["marks"] < 60]

    return {
        "average": average,
        "highest": highest,
        "lowest": lowest,
        "sorted_students": sorted_students,
        "passing_students": passing_students,
        "below_60": below_60
    }

print(analyze_students(students))
print(analyze_students([]))