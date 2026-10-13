# Task
    # 1. age = 22 banao.
    # 2. has_license = True banao.
    # 3. Check karo ki age 18 ya usse zyada hai.
    # 4. and se check karo ki age 18+ aur license bhi hai.
    # 5. or se check karo ki age 18+ ya license hai.
    # 6. not se has_license ki value reverse karo.

# Expected output
    # Age is 18 or above: True
    # Can drive: True
    # Age or license: True
    # License not available: False

age = 22
has_license = True

valid_age = age >= 18

print(f"Age is 18 or above: {valid_age}")
print(f"Car drive: {valid_age and has_license}")
print(f"Age or license: {valid_age or has_license}")
print(f"License not available: {not has_license}")
