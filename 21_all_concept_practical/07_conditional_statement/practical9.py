# Task: Simple ATM withdrawal
    # 1. balance = 5000 banao.
    # 2. withdraw_amount = 2000 banao.
    # 3. Agar withdrawal amount 0 ya usse kam ho, to "Invalid amount" print karo.
    # 4. Warna agar withdrawal amount balance se zyada ho, to "Insufficient balance" print karo.
    # 5. Warna "Withdrawal successful" print karo aur remaining balance bhi print karo.
# Expected output:
    # Withdrawal successful
    # Remaining balance: 3000

balance = 5000
withdraw_amount = 2000

if withdraw_amount <= 0:
    print("Invalid amount")
elif withdraw_amount > balance:
    print("Insufficient balance")
else:
    print("Withdrawal successful")
    print(f"Remaining balance: {balance - withdraw_amount}")