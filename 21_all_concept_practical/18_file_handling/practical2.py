# Goal: File me naya data add karna, bina purana data delete kiye.
# Static values use karna; input() nahi.
# 1. student.txt me pehle se student information likho.
# 2. "a" (append) mode se ek nayi line add karo: City: Ahmedabad
# 3. File ko dobara read karke poora content print karo.
# 4. Dhyan rahe, purana data delete nahi hona chahiye.
# Expected output:
# Name: Amit
# Course: Python
# Marks: 85
# City: Ahmedabad

with open("student.txt", "a") as file:
    file.write(f"\nCity: Ahmedabad")

with open("student.txt", "r") as file:
    for line in file:
        print(line, end="")