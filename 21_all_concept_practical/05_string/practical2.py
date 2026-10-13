# String slicing
    # language = "Python" banao.
    # Pehle 3 characters print karo.
    # Aakhri 3 characters print karo.
    # String ko reverse karke print karo.

# Expected output:
#     First 3 characters: Pyt
#     Last 3 characters: hon
#     Reversed: nohtyP

language = "Python"

print("First 3 characters:", language[0:3])
print("Last 3 characters:", language[-3:])
print("Reversed:", language[::-1])