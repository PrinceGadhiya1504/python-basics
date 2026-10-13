# Student Result Analyzer
# Ek analyze_student(name, *marks, **options) function banao.
# Ismein ye 6 concepts cover karne hain:
# 1. Parameters: name, *marks, **options
# 2. Validation: Agar marks nahi diye gaye, to "No marks provided" return karo.
# 3. Built-in functions: sum(), len(), max(), min()
# 4. Conditional statements: Average 40 ya usse zyada ho to "Pass", warna "Fail".
# 5. Default parameter values: options.get("show_details", True) use karo.
# 6. Dictionary + return: Student ka result dictionary mein return karo.

# Rules:
# - Average = total marks / number of subjects.
# - show_details=False hone par sirf student ka naam aur status return karo.
# - show_details=True hone par naam, total, average, highest mark, lowest mark aur status return karo.

# Test cases:
# print(analyze_student("Amit", 80, 70, 90))
# print(analyze_student("Neha", 30, 35, 25, show_details=False))
# print(analyze_student("Raj"))

# Expected output:
# {'name': 'Amit', 'total': 240, 'average': 80.0, 'highest': 90, 'lowest': 70, 'status': 'Pass'}
# {'name': 'Neha', 'status': 'Fail'}
# No marks provided

def analyze_student(name, *marks, **options):
    if not marks:
        return "No marks provided"

    total = sum(marks)
    average = total / len(marks)
    highest = max(marks)
    lowest = min(marks)

    result = {"name": name, "total": total, "average": average, "highest": highest, "lowest": lowest, "status": "Pass" if average >= 40 else "Fail"}
    if options.get("show_details", True) == False:
        return {"name": name, "status": result["status"]}
    return result

print(analyze_student("Amit", 80, 70, 90))
print(analyze_student("Neha", 30, 35, 25, show_details=False))
print(analyze_student("Raj"))