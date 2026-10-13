# Ek program banao jo:
# 1. Students ka data dictionaries ki list me store kare. Har student ke paas name aur marks hon.
# 2. Function bana kar har student ka result calculate kare:
#    - Marks 80 ya usse zyada: A
#    - Marks 60–79: B
#    - Marks 40–59: C
#    - Marks 40 se kam: Fail
# 3. Loop se har student ka naam, marks aur grade print kare.
# 4. filter() se 80 ya usse zyada marks wale students nikale.
# 5. sorted() se students ko marks ke descending order me sort kare.
# 6. try-except se invalid marks, jaise string marks, handle kare.

# Expected grades:
# Student	Marks	Grade
# Amit	    85	    A
# Neha	    92	    A
# Raj	    35	    Fail
# Priya	    67	    B
# Karan	    48	    C

students = [
    {"name": "Amit", "marks": 85},
    {"name": "Neha", "marks": 92},
    {"name": "Raj", "marks": 35},
    {"name": "Priya", "marks": 67},
    {"name": "Karan", "marks": 48}
]

def get_grade(students):
    if type(students["marks"]) is not int:
        raise TypeError("Marks must be an integer")

    elif not 0 <= students["marks"] <= 100:
        raise ValueError("Marks must be between 0 and 100")

    elif students['marks'] >= 80:
        return "A"

    elif students['marks'] >=60:
        return "B"

    elif students['marks'] >=40:
        return "C"

    else:
        return "Fail"

for s in students:
    try:
        s['grade'] = get_grade(s)
    except TypeError as e:
        s['grade'] = "Invalid"

# 3. Loop se har student ka naam, marks aur grade print kare.
print("\n3. Student Report:")
for student in students:
    print(f"{student['name']} {student['marks']} {student['grade']}")

# 4. filter() se 80 ya usse zyada marks wale students nikale.
print("\n4. Students with A Grade:")
a_grade_students = list(filter(lambda x: x['grade'] == 'A', students))
for student in a_grade_students:
    print(f"Name: {student['name']}, Marks: {student['marks']}")

# 5. sorted() se students ko marks ke descending order me sort kare.
print("\n5. Students sorted by marks (Descending):")
sorted_students = sorted(students, key=lambda x: x['marks'], reverse=True)
for student in sorted_students:
    print(f"Name: {student['name']}, Marks: {student['marks']}, Grade: {student['grade']}")