# Task
    # message = "  Python Programming  " variable banao. Dhyan do: string ke start aur end mein spaces hain.
    # strip() use karke start aur end ki spaces remove karo.
    # replace() use karke "Python" ko "Java" se replace karo.
    # Dono results print karo.

# Expected output:
    # Original:   Python Programming  
    # Stripped: Python Programming
    # Replaced: Java Programming


message = "  Python Programming  "

remove_space = message.strip()
replace_name = remove_space.replace("Python", "Java")

print("Original: " + message)
print("Stripped: " + remove_space)
print("Replaced: " + replace_name)