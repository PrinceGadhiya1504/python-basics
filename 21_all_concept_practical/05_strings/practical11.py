# String validation with isalpha() and isdigit()
# Task
#     1. name = "Prince" variable banao.
#     2. number = "12345" variable banao.
#     3. isalpha() se check karo ki name mein sirf letters hain ya nahi.
#     4. isdigit() se check karo ki number mein sirf digits hain ya nahi.
#     5. Dono results print karo.

# Expected output:
    # Name contains only letters: True
    # Number contains only digits: True

name = "Prince"
number = "12345"

print(f"Name contains only letters: {name.isalpha()}")
print(f"Number contains only digits: {number.isdigit()}")