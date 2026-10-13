# Task: Weekday or weekend
    # 1. day = "Sunday" banao.
    # 2. match day: use karo.
    # 3. "Saturday" ya "Sunday" hone par "Weekend" print karo.
    # 4. "Monday" se "Friday" tak kisi bhi din par "Weekday" print karo.
    # 5. Kisi aur value par "Invalid day" print karo.
# Expected output:
    # Weekend

day = "Sunday"

match day:
    case "Saturday" | "Sunday":
        print("Weekend")
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        print("Weekday")
    case _:
        print("Invalid day")