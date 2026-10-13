# String replacement aur case conversion
# Task
#     1. text = "I love python programming" variable banao.
#     2. String ko uppercase mein convert karo.
#     3. "python" ko "Java" se replace karo.
#     4. Check karo ki original string mein "python" present hai ya nahi, in operator ka use karke.
#     5. Teeno results print karo.

# Expected output
#     Uppercase: I LOVE PYTHON PROGRAMMING
#     Replaced: I love Java programming
#     Contains python: True

text = "I love python programming"

upper_text = text.upper()
replace_text = text.replace("python", "Java")
is_exist = "python" in text

print(f"Uppercase: {upper_text}")
print(f"Replaced: {replace_text}")
print(f"Contains python: {is_exist}")