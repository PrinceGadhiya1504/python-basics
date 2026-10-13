# Ek function analyze_students(students) banao:
# 1. Tuple empty ho toh "No students available" return karo.
# 2. len() se total students nikalo.
# 3. sum() se average marks calculate karo.
# 4. max() aur min() se highest aur lowest marks wale poore tuples nikalo.
# 5. sorted() aur lambda se marks descending order mein sort karo.
# 6. List comprehension se 60 ya usse zyada marks wale poore tuples nikalo.
# 7. Set comprehension se unique grades nikalo.
# 8. tuple() ka use karke passing students ki list ko tuple mein convert karo.
# 9. Saare results dictionary mein return karo.
# 10. Normal aur empty tuple dono test karo.

# Expected output
# {
#     "total_students": 5,
#     "average_marks": 71.8,
#     "highest_student": ("Neha", 92, "A+"),
#     "lowest_student": ("Raj", 45, "C"),
#     "sorted_students": [
#         ("Neha", 92, "A+"),
#         ("Priya", 88, "A"),
#         ("Amit", 78, "A"),
#         ("Jay", 56, "B"),
#         ("Raj", 45, "C")
#     ],
#     "passing_students": [
#         ("Amit", 78, "A"),
#         ("Neha", 92, "A+"),
#         ("Priya", 88, "A")
#     ],
#     "unique_grades": {"A", "A+", "B", "C"},
#     "passing_students_tuple": (
#         ("Amit", 78, "A"),
#         ("Neha", 92, "A+"),
#         ("Priya", 88, "A")
#     )
# }
# No students available

students = (
    ("Amit", 78, "A"),
    ("Neha", 92, "A+"),
    ("Raj", 45, "C"),
    ("Priya", 88, "A"),
    ("Jay", 56, "B")
)

def analyze_students(students):
    if not students:
        return "No students available"

    total_student = len(students)
    average_marks = sum(student[1] for student in students)/ total_student
    highest_marks = max(students, key=lambda x: x[1])
    lowest_marks = min(students, key=lambda x: x[1])
    sorted_marks = sorted(students, key=lambda x: x[1], reverse=True)
    marks_60_plus = [student for student in students if student[1] >= 60]
    unique_grade = set(student[2] for student in students)
    passing_student = tuple(marks_60_plus)
    
    return{
        "total_students": total_student,
        "average_marks": average_marks,
        "highest_marks": highest_marks,
        "lowest_marks": lowest_marks,
        "sorted_marks": sorted_marks,
        "marks_60_plus": marks_60_plus,
        "unique_grade": unique_grade,
        "passing_student": passing_student
    }

print(analyze_students(students))
print(analyze_students(()))
