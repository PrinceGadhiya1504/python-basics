# Question
# Ek Python program banao jo user se ye 4 details input le:
# - Student ka name
# - Age
# - City
# - Course name
# Input lene ke baad saari details ek proper format mein print karo.

# Expected result
# Example terminal output
# Enter student name: Prince
# Enter student age: 23
# Enter student city: Ahmedabad
# Enter course name: Python
# ----- Student Details -----
# Name: Prince
# Age: 23
# City: Ahmedabad
# Course: Python

# Rules
# 1. User se saari details input() ki help se leni hain.
# 2. Age ko integer type mein convert karna hai.
# 3. Output ko expected result ke format mein print karna hai.
# 4. Abhi functions ya classes use nahi karni hain.

name = input("Enter student name: ")
age = int(input("Enter student age: "))
city = input("Enter student city: ")
course = input("Enter student course: ")

print("\n----- Student Details -----")
print("Name:", name)
print("Age:", age)
print("City:", city)
print("Course:", course)