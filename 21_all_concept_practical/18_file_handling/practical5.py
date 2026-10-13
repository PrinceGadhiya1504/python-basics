# Tumhe program banana hai jo:
# 1. os module import kare.
# 2. Check kare ki notes.txt file exist karti hai ya nahi, using os.path.exists().
# 3. Agar file exist karti hai, to message print kare: File exists.
# 4. File ko os.remove() se delete kare.
# 5. Dobara check karke print kare: File exists after deletion: False.
# Expected output:
# File exists
# File exists after deletion: False

import os

if os.path.exists("notes.txt"):
    print("File exists")
    os.remove("notes.txt")
    print("File exists after deletion:", os.path.exists("notes.txt"))
else:
    print("File does not exist")