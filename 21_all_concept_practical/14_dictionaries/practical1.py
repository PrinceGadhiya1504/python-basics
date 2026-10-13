# Ek function analyze_students(students) banao jo:
# 1. len() se total students nikale.
# 2. keys() se saare student names nikale.
# 3. values() se saare marks nikale.
# 4. items() se name aur marks ke pairs nikale.
# 5. get() se "Neha" ke marks nikale.
# 6. get() se "Jay" ke marks nikale; student nahi ho to default 0 return ho.
# 7. max() aur min() se highest aur lowest marks nikale.
# 8. Dictionary comprehension se sirf un students ka naya dictionary banao jinke marks 80 ya usse zyada hain.
# 9. sum() se total marks aur average marks nikale.
# 10. Saare results dictionary mein return kare.
# Expected checks:
# - Total students: 4
# - Neha ke marks: 92
# - Jay ke marks: 0
# - Highest marks: 96
# - Lowest marks: 74
# - Average marks: 86.75

students = {
    "Amit": 85,
    "Neha": 92,
    "Raj": 74,
    "Priya": 96
}

def analyze_students(students):
    total_student = len(students)
    student_name = students.keys()
    student_mark = students.values()
    students.items()
    neha_mark = students.get('Neha')
    jay_mark = students.get('Jay',0)
    high_mark = max(students.values())
    low_mark = min(students.values())
    mark_80_plush = {student: marks for student, marks in students.items() if marks >= 80}
    average_marks = sum(students.values())/len(students)
    total_marks = sum(students.values())
    return {
        "total_student": total_student,
        "student_name": student_name,
        "student_mark": student_mark,
        "students": students,
        "neha_mark": neha_mark,
        "jay_mark": jay_mark,
        "high_mark": high_mark,
        "low_mark": low_mark,
        "mark_80_plush": mark_80_plush,
        "average_marks": average_marks,
        "total_marks": total_marks
    }

print(analyze_students(students))

    