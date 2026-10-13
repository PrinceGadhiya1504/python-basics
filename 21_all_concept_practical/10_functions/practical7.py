# Task:
    # 1. check_even(number) naam ka function banao.
    # 2. Agar number even ho, to "Even" return karo.
    # 3. Agar number even nahi ho, to "Odd" return karo.
    # 4. Function ko 7 ke saath call karo aur returned value print karo.
# Expected output:
    # Odd

def check_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(check_even(7))
    