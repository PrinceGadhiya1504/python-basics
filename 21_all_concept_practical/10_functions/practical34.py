# Task:
# 1. show_students(names, marks) naam ka function banao.
# 2. Function ke andar zip() se har student ka naam aur marks pair karo.
# 3. Har pair ko name: marks format mein print karo.
# 4. Function ko in lists ke saath call karo:
#    - names = ["Amit", "Neha", "Raj"]
#    - marks = [85, 90, 78]
# Expected output:
# Amit: 85
# Neha: 90
# Raj: 78

def show_students(names, marks):
    for name, mark in zip(names, marks):
        print(f"{name}: {mark}")

names = ["Amit", "Neha", "Raj"]
marks = [85, 90, 78]
show_students(names, marks)