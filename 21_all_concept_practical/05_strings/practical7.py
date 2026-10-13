# find() method
    # 1. sentence = "Python is easy and Python is powerful" banao.
    # 2. find() use karke "Python" ka pehla index find karo.
    # 3. find() use karke "Java" ka index find karo.
    # 4. Dono results print karo.

# Expected output:
    # First Python index: 0
    # Java index: -1

sentence = "Python is easy and Python is powerful"

print(f"First Python index: {sentence.find('Python')}")
print(f"Java index: {sentence.find('Java')}")