# Ek function read_file(filename) banao jo:
# 1. try block mein file ko read mode ("r") mein open kare.
# 2. File ka content read karke return kare.
# 3. Agar file exist nahi karti, to FileNotFoundError handle karke "File not found" return kare.
# 4. Agar file read karne mein permission issue aaye, to PermissionError handle karke "Permission denied" return kare.
# 5. else block mein successful reading ka message print kare.
# 6. finally mein "File operation completed" print kare.
# 7. In dono cases ko test kare:

# Important: sample.txt banakar usmein kuch text likho, jaise Python learning. missing.txt file create mat karna, taaki error handling test ho sake.
# Expected results:
# - Existing file → uska content return ho.
# - Missing file → "File not found" return ho.

def read_file(filename):
    try:
        file = open(filename, 'r')
        content = file.read()
        file.close()
    except FileNotFoundError:
        return "File not found"
    except PermissionError:
        return "Permission denied"
    else:
        print("File reading successful")
        return content
    finally:
        print("File operation completed")

print(read_file("sample.txt"))
print(read_file("missing.txt"))