# Strings: Multiple conditions
# Task
    # 1. username = "Prince123" banao.
    # 2. Check karo ki username "Prince" se start hota hai ya nahi.
    # 3. Check karo ki username mein "123" present hai ya nahi.
    # 4. Dono conditions ko and operator se combine karo.
    # 5. Final result print karo.
# Expected output:
    # Starts with Prince: True
    # Contains 123: True
    # Both conditions are True: True

username = "Prince123"

print(f"Starts with Prince: {username.startswith('Prince')}")
print(f"Contains 123: {'123' in username}")
print(f"Both conditions are True: {username.startswith('Prince') and '123' in username}")