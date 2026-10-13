# Ek function analyze_performance(students) banao.
# 1. Empty list ho toh "No student data available" return karo.
# 2. len() se total students nikalo.
# 3. sum() se average marks calculate karo.
# 4. max() se highest marks wale student ka poora dictionary nikalo.
# 5. sorted() aur lambda se marks ko descending order mein sort karo.
# 6. List comprehension se un students ke poore dictionaries nikalo jinke marks 60 ya usse zyada hain.
# 7. filter() se un students ke poore dictionaries nikalo jinki attendance 75 ya usse zyada hai.
# 8. Set comprehension se unique attendance values nikalo.
# 9. Sabhi results dictionary mein return karo.
# 10. Normal aur empty list dono test karo.

# Expected output
# {
#     "total_students": 5,
#     "average_marks": 71.0,
#     "highest_marks_student": {
#         "name": "Neha",
#         "marks": 92,
#         "attendance": 95
#     },
#     "sorted_students": [
#         {"name": "Neha", "marks": 92, "attendance": 95},
#         {"name": "Priya", "marks": 88, "attendance": 72},
#         {"name": "Amit", "marks": 78, "attendance": 85},
#         {"name": "Jay", "marks": 55, "attendance": 80},
#         {"name": "Raj", "marks": 42, "attendance": 60}
#     ],
#     "passing_students": [
#         {"name": "Amit", "marks": 78, "attendance": 85},
#         {"name": "Neha", "marks": 92, "attendance": 95},
#         {"name": "Priya", "marks": 88, "attendance": 72}
#     ],
#     "attendance_75_plus": [
#         {"name": "Amit", "marks": 78, "attendance": 85},
#         {"name": "Neha", "marks": 92, "attendance": 95},
#         {"name": "Jay", "marks": 55, "attendance": 80}
#     ],
#     "unique_attendance": {60, 72, 80, 85, 95}
# }
# No student data available


students = [
    {"name": "Amit", "marks": 78, "attendance": 85},
    {"name": "Neha", "marks": 92, "attendance": 95},
    {"name": "Raj", "marks": 42, "attendance": 60},
    {"name": "Priya", "marks": 88, "attendance": 72},
    {"name": "Jay", "marks": 55, "attendance": 80}
]

def analyze_performance(students):
    if not students:
        return "No student data available"

    total_student = len(students)
    average_marks = sum(student['marks'] for student in students)/ total_student
    highest_marks = max(students, key = lambda x : x['marks'])
    sorted_marks = sorted(students, key = lambda x : x['marks'], reverse=True)
    passing_students = [
        student for student in students
        if student['marks'] >= 60
    ]
    attendance_75_plus = list(filter(lambda x : x['attendance'] >= 75, students))
    unique_attendance = {
        student['attendance'] for student in students
    }
    return {
        "total_students" : total_student,
        "average_marks" : average_marks,
        "highest_marks_student" : highest_marks,
        "sorted_students" : sorted_marks,
        "passing_students" : passing_students,
        "attendance_75_plus" : attendance_75_plus,
        "unique_attendance" : unique_attendance
    }

print(analyze_performance(students))
print(analyze_performance([]))