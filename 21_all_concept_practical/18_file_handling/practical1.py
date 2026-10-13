# Ek program banao jo student.txt file ke saath kaam kare:
# 1. open() se file ko write mode ("w") mein open kare.
# 2. File mein student ka naam, course aur marks likhe.
# 3. with open() ka use karke file read kare.
# 4. File ka complete content print kare.
# 5. readline() se pehli line read karna bhi demonstrate kare.
# 6. readlines() se saari lines list mein read kare.
# Ye static data use karo:
# name = "Amit"
# course = "Python"
# marks = 85

name = "Amit"
course = "Python"
marks = 85

with open("student.txt", 'w') as file:
    file.write(f"Name: {name}\n")
    file.write(f"Course: {course}\n")
    file.write(f"Marks: {marks}\n")

with open("student.txt", 'r') as file:
    for line in file:
        print(line, end="")

with open("student.txt", 'r') as file:
    print(file.readline())

with open("student.txt", 'r') as file:
    print(file.readlines())

