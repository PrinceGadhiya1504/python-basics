# Task: Grade calculator
    # 1. marks = 78 variable banao.
    # 2. Agar marks 90 ya usse zyada hon, to "Grade A" print karo.
    # 3. Warna agar marks 75 ya usse zyada hon, to "Grade B" print karo.
    # 4. Warna agar marks 35 ya usse zyada hon, to "Grade C" print karo.
    # 5. Baaki cases mein "Fail" print karo.
# Expected output:
    # Grade B

marks = 78

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 35:
    print("Grade C")
else:
    print("Fail")