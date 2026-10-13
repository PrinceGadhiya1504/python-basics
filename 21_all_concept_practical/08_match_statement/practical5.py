# Task: Simple menu system
    # 1. choice = 2 banao.
    # 2. match choice: use karo.
    # 3. 1 hone par "Start Game" print karo.
    # 4. 2 hone par "Settings" print karo.
    # 5. 3 hone par "Exit" print karo.
    # 6. Kisi aur value par "Invalid choice" print karo.
# Expected output:
    # Settings

choice = 2

match choice:
    case 1:
        print("Start Game")
    case 2:
        print("Settings")
    case 3:
        print("Exit")
    case _:
        print("Invalid choice")