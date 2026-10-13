# Ek function manage_enrollment(python_students, java_students) banao jo:
# 1. Dono courses mein enrolled unique students ka set nikale.
# 2. Dono courses mein common students nikale.
# 3. Python course mein "Karan" ko add() kare.
# 4. Java course mein "Mihir" aur "Riya" ko update() se add kare.
# 5. Python course se "Priya" ko remove() kare.
# 6. Java course se "Amit" ko discard() kare. Agar student nahi hai, tab bhi error nahi aana chahiye.
# 7. Check kare ki "Neha" Python course mein enrolled hai ya nahi.
# 8. Python students ke set ki copy banaye.
# 9. Python students ki total count nikale.
# 10. Dono updated sets aur baaki results dictionary mein return kare.
# Important: pop() aur clear() ko bhi practice karna hai, lekin pop() randomly koi element remove karta hai aur clear() poora set empty karta hai. Isliye inhe copies par use karna, taaki original enrollment data safe rahe.
# Expected output ke important checks
# - Original unique students: {"Amit", "Neha", "Raj", "Priya", "Jay"}
# - Original common students: {"Neha", "Raj"}
# - Updated Python students: {"Amit", "Neha", "Raj", "Karan"}
# - Updated Java students: {"Neha", "Jay", "Raj", "Mihir", "Riya"}
# - "Neha" Python course mein enrolled: True
# - Updated Python students ki count: 4

python_students = {"Amit", "Neha", "Raj", "Priya"}
java_students = {"Neha", "Jay", "Raj"}

def manage_enrollment(python_students, java_students):
    unique_students = python_students.union(java_students)
    common_students = python_students.intersection(java_students)
    python_students.add("Karan")
    java_students.update(["Mihir", "Riya"])
    python_students.remove('Priya')
    java_students.discard("Amit")
    is_neha_enrolled = "Neha" in python_students
    python_copy = python_students.copy()
    python_copy.pop()
    python_copy.clear()
    python_count = len(python_students)
    
    return {
        "unique_students": unique_students,
        "common_students": common_students,
        "python_students": python_students,
        "java_students": java_students,
        "is_neha_enrolled": is_neha_enrolled,
        "python_copy": python_copy,
        "python_count": python_count
    }


print(manage_enrollment(python_students, java_students))