# Ek program banao jo:
# 1. notes.txt ko "w" mode me open karke Python File Handling likhe.
# 2. File ko "a" mode me open karke next line me Learning read and write methods add kare.
# 3. File ko "r" mode me open karke poora content read() se print kare.
# Expected output:
# Python File Handling
# Learning read and write methods

with open("notes.txt", "w") as file:
    file.write("Python File Handling\n")
with open("notes.txt", "a") as file:
    file.write("Learning read and write methods\n")
with open("notes.txt", "r") as file:
    print(file.read())