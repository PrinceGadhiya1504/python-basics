# Task:
# 1. check_integer(value) naam ka function banao.
# 2. isinstance() se check karo ki value integer hai ya nahi.
# 3. Result ko return karo.
# 4. check_integer(25) call karke result print karo.
# Expected output:
# True

def check_integer(value):
    if isinstance(value, int):
        return True
    else:
        return False

print(check_integer(25))