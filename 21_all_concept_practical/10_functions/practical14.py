# Task:
    # 1. square(number) function banao, jo number ka square return kare.
    # 2. display_square(number) function banao.
    # 3. display_square() ke andar square(number) call karo aur returned value print karo.
    # 4. display_square(4) call karo.
# Expected output:
    # 100

def square(number):
    return number * number

def display_square(number):
    print(square(number))

display_square(10)