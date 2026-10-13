# Ek function generate_report(students, subjects) banao jo:
# 1. Agar students ya subjects empty ho, toh "Data is missing" return kare.
# 2. len() se total students count kare.
# 3. Tuple unpacking se har student ka name, marks aur grade nikale.
# 4. Slicing se pehle 3 students ka tuple nikale.
# 5. enumerate() se students ko 1 se numbering de.
# 6. zip() se students aur subjects ko pair kare.
# 7. List comprehension se 60 ya usse zyada marks wale students ke poore tuples nikale.
# 8. sum() aur len() se average marks calculate kare.
# 9. max() se highest marks wala poora tuple nikale.
# 10. Results dictionary mein return kare aur normal aur empty data dono test kare.

# Expected output
# {
#     "total_students": 5,
#     "first_three_students": (
#         ("Amit", 78, "A"),
#         ("Neha", 92, "A+"),
#         ("Raj", 45, "C")
#     ),
#     "numbered_students": [
#         (1, ("Amit", 78, "A")),
#         (2, ("Neha", 92, "A+")),
#         (3, ("Raj", 45, "C")),
#         (4, ("Priya", 88, "A")),
#         (5, ("Jay", 56, "B"))
#     ],
#     "student_subject_pairs": [
#         (("Amit", 78, "A"), "Python"),
#         (("Neha", 92, "A+"), "SQL"),
#         (("Raj", 45, "C"), "Excel"),
#         (("Priya", 88, "A"), "Power BI"),
#         (("Jay", 56, "B"), "Statistics")
#     ],
#     "passing_students": [
#         ("Amit", 78, "A"),
#         ("Neha", 92, "A+"),
#         ("Priya", 88, "A")
#     ],
#     "average_marks": 71.8,
#     "highest_student": ("Neha", 92, "A+")
# }
# Data is missing

students = (
    ("Amit", 78, "A"),
    ("Neha", 92, "A+"),
    ("Raj", 45, "C"),
    ("Priya", 88, "A"),
    ("Jay", 56, "B")
)

subjects = ("Python", "SQL", "Excel", "Power BI", "Statistics")

def generate_report(students, subjects):
    if not students or not subjects:
        return "Data is missing"

    total_student = len(students)
    
    for name, marks, grade in students:
        print(name, marks, grade)

    first_3_student = students[:3]

    numbered_students = list(enumerate(students, start=1))
    student_subject_pairs = list(zip(students, subjects))

    passing_student = [student for student in students if student[1] >= 60]

    average_marks = sum(student[1] for student in students) / total_student

    highest_student = max(students, key=lambda x: x[1])

    return {
        "total_students": total_student,
        "first_3_student": first_3_student,
        "numbered_students": numbered_students,
        "student_subject_pairs": student_subject_pairs,
        "passing_student": passing_student,
        "average_marks": average_marks,
        "highest_student": highest_student
    }

print(generate_report(students, subjects))
print(generate_report((), ()))