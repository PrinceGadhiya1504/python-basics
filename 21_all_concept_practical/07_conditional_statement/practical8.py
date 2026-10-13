# Task: Movie ticket eligibility
    # 1. age = 16 banao.
    # 2. has_parent = True banao.
    # 3. Pehle check karo ki age 18 ya usse zyada hai.
    # 4. Agar age 18 se kam hai, to check karo ki has_parent True hai ya nahi.
    # 5. Agar age 18+ hai, to "Ticket allowed" print karo.
    # 6. Agar age 18 se kam hai aur parent saath hai, to "Ticket allowed with parent" print karo.
    # 7. Agar age 18 se kam hai aur parent saath nahi hai, to "Ticket not allowed" print karo.
# Expected output:
    # Ticket allowed with parent

age = 16
has_parent = True

if age >= 18:
    print("Ticket allowed")
elif age < 18 and has_parent:
    print("Ticket allowed with parent")
else:
    print("Ticket not allowed")

    