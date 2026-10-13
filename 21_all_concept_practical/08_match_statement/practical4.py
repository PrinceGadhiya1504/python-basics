# Task: Number classification
    # 1. number = 15 banao.
    # 2. match number: use karo.
    # 3. case n if n > 0: se positive number check karo.
    # 4. case 0: se zero check karo.
    # 5. case _: se negative number handle karo.
# Expected output:
    # Positive number

number = 15

match number:
    case n if n > 0:
        print("Positive number")
    case 0:
        print("Zero")
    case _:
        print("Negative number")