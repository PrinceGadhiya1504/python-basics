# Task: Email validation (basic)
    # 1. email = "prince@gmail.com" variable banao.
    # 2. Check karo ki email mein "@" present hai ya nahi.
    # 3. Check karo ki email ".com" par end hota hai ya nahi.
    # 4. Dono conditions ko and se combine karo.
    # 5. Final result print karo.
# Hint: in, endswith() aur and use karo.

# Expected output:
    # Contains @: True
    # Ends with .com: True
    # Basic validation: True

email = "prince@gmail.com" 

contains_at = '@' in email
ends_with_com = email.endswith('.com')

print(f"Contains @: {contains_at}")
print(f"Ends with .com: {ends_with_com}")
print(f"Basic validation: {contains_at and ends_with_com}")