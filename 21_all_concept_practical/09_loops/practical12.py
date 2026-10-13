# Task: Countdown with early stop
    # 1. count = 10 banao.
    # 2. while count > 0: loop chalao.
    # 3. Har iteration mein count print karo.
    # 4. Agar count == 6 ho, to break se loop stop karo.
    # 5. Har iteration mein count ko 1 se decrease karo, lekin dhyan rahe ki 6 par loop rukna chahiye.
# Expected output:
    # 10
    # 9
    # 8
    # 7
    # 6

count = 10

while count > 0:
    print(count)
    if count == 6:
        break
    count -= 1