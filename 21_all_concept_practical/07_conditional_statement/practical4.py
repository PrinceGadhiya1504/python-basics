# Task: Discount eligibility
    # 1. age = 25 banao.
    # 2. purchase_amount = 1500 banao.
    # 3. Agar age 18 ya usse zyada aur purchase amount 1000 ya usse zyada hai, to "Discount eligible" print karo.
    # 4. Warna "Not eligible for discount" print karo.
# Expected output:
    # Discount eligible

age = 25
purchase_amount = 1500

if age >= 18 and purchase_amount >= 1000:
    print("Discount eligible")
else:
    print("Not eligible for discount")    