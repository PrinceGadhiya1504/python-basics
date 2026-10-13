# Task:
# 1. zip() se har student ka naam aur marks pair karo.
# 2. enumerate() se har student ko 1 se start hone wala serial number do.
# 3. Har student ke liye Name: Marks format mein print karo.
# 4. filter() aur lambda se passing marks (40 ya usse zyada) ki list banao.
# 5. map() aur lambda se sabhi marks mein 5 bonus marks add karo.
# 6. any() se check karo ki koi student fail hua hai ya nahi.
# 7. all() se check karo ki sabhi students pass hue hain ya nahi.

# Expected output:
# 1. Amit: 85
# 2. Neha: 38
# 3. Raj: 67
# 4. Priya: 92
# Passing marks: [85, 67, 92]
# Bonus marks: [90, 43, 72, 97]
# Any student failed: True
# All students passed: False

names = ["Amit", "Neha", "Raj", "Priya"]
marks = [85, 38, 67, 92]

for sr_num, (name, mark) in enumerate(zip(names, marks), start=1):
    print(f"{sr_num}. {name}: {mark}")

passing_marks = list(filter(lambda x : x >= 40, marks))
print(f"Passing marks: {passing_marks}")

bonus_marks = list(map(lambda x : x + 5, marks))
print(f"Bonus marks: {bonus_marks}")

failed = any(x < 40 for x in marks)
print(f"Any student failed: {failed}")

all_passed = all(x >= 40 for x in marks)
print(f"All students passed: {all_passed}")
