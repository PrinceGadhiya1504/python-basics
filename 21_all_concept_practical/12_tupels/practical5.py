# Ek function build_student_report(names, marks, grades) banao:
# 1. Agar koi tuple empty ho ya teeno tuples ki length alag ho, toh "Invalid student data" return karo.
# 2. zip() se student records banao: (name, marks, grade).
# 3. enumerate() se records ko 1 se numbering do.
# 4. filter() se 60 se kam marks wale poore student records nikalo.
# 5. sorted() aur lambda se records ko marks ke descending order mein sort karo.
# 6. any() se check karo ki koi student 90 ya usse zyada marks laya hai.
# 7. all() se check karo ki sabhi students ke marks 35 ya usse zyada hain.
# 8. tuple() se filtered failing records ko tuple mein convert karo.
# 9. Saare results dictionary mein return karo.
# 10. Normal data aur invalid-length data dono test karo.
# Expected output
# {
#     "student_records": (
#         ("Amit", 78, "A"),
#         ("Neha", 92, "A+"),
#         ("Raj", 45, "C"),
#         ("Priya", 88, "A"),
#         ("Jay", 56, "B")
#     ),
#     "numbered_records": [
#         (1, ("Amit", 78, "A")),
#         (2, ("Neha", 92, "A+")),
#         (3, ("Raj", 45, "C")),
#         (4, ("Priya", 88, "A")),
#         (5, ("Jay", 56, "B"))
#     ],
#     "failing_students": (
#         ("Raj", 45, "C"),
#         ("Jay", 56, "B")
#     ),
#     "sorted_records": [
#         ("Neha", 92, "A+"),
#         ("Priya", 88, "A"),
#         ("Amit", 78, "A"),
#         ("Jay", 56, "B"),
#         ("Raj", 45, "C")
#     ],
#     "any_90_plus": True,
#     "all_pass_35": True
# }
# Invalid student data

names = ("Amit", "Neha", "Raj", "Priya", "Jay")
marks = (78, 92, 45, 88, 56)
grades = ("A", "A+", "C", "A", "B")

def build_student_report(names, marks, grades):
    if not names or not marks or not grades or len(names) != len(marks) or len(marks) != len(grades):
        return "Invalid student data"

    student_records = tuple(zip(names, marks, grades))
    numbered_records = list(enumerate(student_records, 1))
    failing_students = tuple(filter(lambda x: x[1] < 60, student_records))
    sorted_records = sorted(student_records, key=lambda x: x[1], reverse=True)
    any_90_plus = any(x[1] >= 90 for x in student_records)
    all_pass_35 = all(x[1] >= 35 for x in student_records)

    return {
        "student_records": student_records,
        "numbered_records": numbered_records,
        "failing_students": failing_students,
        "sorted_records": sorted_records,
        "any_90_plus": any_90_plus,
        "all_pass_35": all_pass_35
    }

print(build_student_report(names, marks, grades))
print(build_student_report((), (1, 2), (3, 4)))