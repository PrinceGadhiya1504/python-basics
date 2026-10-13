# String scenario: startswith() with multiple values
# Task
    # 1. filename = "photo.png" variable banao.
    # 2. Check karo ki filename .png par end hota hai ya nahi.
    # 3. Check karo ki filename .jpg par end hota hai ya nahi.
    # 4. Dono results print karo.

# Expected output:
    # Is PNG file: True
    # Is JPG file: False

filename = "photo.png"

print(f"Is PNG file: {filename.endswith('.png')}")
print(f"Is JPG file: {filename.endswith('.jpg')}")