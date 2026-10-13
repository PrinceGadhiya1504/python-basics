# Ek function update_student_records(students) banao jo:
# 1. copy() se original dictionary ki copy banaye.
# 2. Check kare ki "Neha" dictionary mein hai ya nahi.
# 3. get() se "Jay" ke marks nikale; absent hone par 0 mile.
# 4. update() se "Jay": 88 aur "Mihir": 79 add kare.
# 5. setdefault() se "Amit" ka existing score change kiye bina default 100 set karne ki koshish kare.
# 6. pop() se "Raj" ko remove kare aur uske marks save kare.
# 7. popitem() se last inserted record remove kare aur save kare.
# 8. del se "Priya" ko remove kare.
# 9. Dictionary comprehension se 80 ya usse zyada marks wale students ka naya dictionary banaye.
# 10. Saare results dictionary mein return kare.
# Important: Saare updates copied dictionary par karna, taaki original students dictionary safe rahe.

students = {
    "Amit": 85,
    "Neha": 92,
    "Raj": 74,
    "Priya": 96
}

def update_student_records(students):
    copy_students = students.copy()
    neha_in_dict = "Neha" in copy_students
    jay_mark = copy_students.get("Jay",0)
    copy_students.update({"Jay": 88, "Mihir": 79})
    copy_students.setdefault("Amit",100)
    raj_mark = copy_students.pop("Raj")
    pop_item = copy_students.popitem()
    del copy_students["Priya"]
    marks_80_plus = {student: marks for student, marks in copy_students.items() if marks >= 80}
    
    return {
        "copy_students": copy_students,
        "neha_in_dict": neha_in_dict,
        "jay_mark": jay_mark,
        "raj_mark": raj_mark,
        "pop_item": pop_item,
        "marks_80_plus": marks_80_plus
    }

print(update_student_records(students))