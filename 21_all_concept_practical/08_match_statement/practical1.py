# Task: Day name finder
    # 1. day_number = 3 variable banao.
    # 2. match statement use karo.
    # 3. 1 hone par "Monday" print karo.
    # 4. 2 hone par "Tuesday" print karo.
    # 5. 3 hone par "Wednesday" print karo.
    # 6. 4 hone par "Thursday" print karo.
    # 7. 5 hone par "Friday" print karo.
    # 8. Kisi aur value par "Invalid day number" print karo.
# Expected output:
    # Wednesday

day_number = 3

match day_number:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case _:
        print("Invalid day number")

