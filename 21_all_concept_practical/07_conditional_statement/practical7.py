# Task: Temperature checker
    # 1. temperature = 32 banao.
    # 2. Agar temperature 40 ya usse zyada ho, to "Very hot" print karo.
    # 3. Warna agar temperature 30 ya usse zyada ho, to "Hot" print karo.
    # 4. Warna agar temperature 20 ya usse zyada ho, to "Pleasant" print karo.
    # 5. Baaki cases mein "Cold" print karo.
# Expected output:
    # Hot

temperature = 32

if temperature >= 40:
    print("Very hot")
elif temperature >= 30:
    print("Hot")
elif temperature >= 20:
    print("Pleasant")
else:
    print("Cold")