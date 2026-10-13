# Task:
# 1. get_student_age(student) naam ka function banao.
# 2. Function dictionary se "age" ki value get() method se return kare.
# 3. Agar "age" key na ho, to default value 0 return ho.
# 4. Function ko {"name": "Prince", "age": 22} ke saath call karke result print karo.
# Expected output:
# 22

def get_student_age(student):
    return student.get("age", 0)

print(get_student_age({"name": "Prince", "age": 22}))