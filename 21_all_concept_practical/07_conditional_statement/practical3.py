# Task: Login check
    # 1. username = "Prince" banao.
    # 2. password = "python123" banao.
    # 3. Pehle check karo ki username "Prince" hai ya nahi.
    # 4. Agar username sahi hai, tabhi password check karo.
    # 5. Password "python123" sahi hai to "Login successful" print karo.
    # 6. Username galat ho to "Invalid username" print karo.
    # 7. Username sahi, lekin password galat ho to "Invalid password" print karo.
# Expected output:
    # Login successful

username = "Prince"
password = "python123"

if username == "Prince":
    if password == "python123":
        print("Login successful")
    else:
        print("Invalid password")
else:
    print("Invalid username")