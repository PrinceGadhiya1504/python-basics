# 1. sorted() aur lambda se students ko marks ke ascending order me sort karo.
# 2. Students ko marks ke descending order me sort karo.
# 3. filter() aur lambda se sirf 80 ya usse zyada marks wale students select karo.
# 4. map() aur lambda se har student ko is format me convert karo: "Amit scored 85 marks".
# 5. max() aur lambda se highest marks wale student ka tuple find karo.
# 6. min() aur lambda se lowest marks wale student ka tuple find karo.

# Expected output:
# Ascending: [('Karan', 68), ('Raj', 76), ('Amit', 85), ('Neha', 92), ('Priya', 92)]
# Descending: [('Neha', 92), ('Priya', 92), ('Amit', 85), ('Raj', 76), ('Karan', 68)]
# 80 or above: [('Amit', 85), ('Neha', 92), ('Priya', 92)]
# Student messages: ['Amit scored 85 marks', 'Neha scored 92 marks', 'Raj scored 76 marks', 'Priya scored 92 marks', 'Karan scored 68 marks']
# Highest: ('Neha', 92)
# Lowest: ('Karan', 68)

students = [
    ("Amit", 85),
    ("Neha", 92),
    ("Raj", 76),
    ("Priya", 92),
    ("Karan", 68)
]

sorted_marks_asc = sorted(students, key = lambda x : x[1])
sorted_marks_desc = sorted(students, key = lambda x : x[1], reverse=True)
grater_80 = list(filter(lambda x : x[1] >= 80, students))
message = list(map(lambda x : f"{x[0]} scored {x[1]} marks", students))
max_marks = max(students, key = lambda x : x[1])
min_marks = min(students, key = lambda x : x[1])


print("Ascending:", sorted_marks_asc)
print("Descending:", sorted_marks_desc)
print("80 or above:", grater_80)
print("Student messages:", message)
print("Highest marks:", max_marks)
print("Lowest marks:", min_marks)