# Task: count() method
    # 1. sentence = "python is easy and python is powerful" variable banao.
    # 2. count() use karke check karo ki "python" kitni baar aaya hai.
    # 3. "is" kitni baar aaya hai, woh bhi check karo.
    # 4. Dono results print karo.

# Expected output:
    # python count: 2
    # is count: 2

sentence = "python is easy and python is powerful"
python_count = sentence.count("python")
is_count = sentence.count("is")

print(f"python count: {python_count}")
print(f"is count: {is_count}")