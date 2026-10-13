# Task:
# 1. show_student(student) naam ka function banao.
# 2. Function ke andar dictionary se student ka name aur age access karo.
# 3. Dono values ko alag-alag print karo.
# 4. Function ko is dictionary ke saath call karo: {"name": "Prince", "age": 22}

# Expected output:
# Prince
# 22


def show_student(student):
    print(student['name'])
    print(student['age'])

show_student({"name": "Prince", "age": 22})