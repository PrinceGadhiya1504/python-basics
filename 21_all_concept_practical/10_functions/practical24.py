# Task:
# 1. show_profile(name, age) naam ka function banao.
# 2. Function ke andar name aur age print karo, har value alag line mein.
# 3. Ek dictionary banao: profile = {"name": "Prince", "age": 22}.
# 4. Function ko show_profile(**profile) se call karo.
# Expected output:
# Prince
# 22

def show_profile(name, age):
    print(name)
    print(age)

profile = {"name": "Prince", "age": 22}
show_profile(**profile)