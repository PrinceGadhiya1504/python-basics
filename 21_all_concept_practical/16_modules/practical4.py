# os aur pathlib karenge.
# Ismein ek practical se ye concepts cover karenge:
# - os.getcwd() — current working directory
# - os.listdir() — folder ki files aur folders
# - os.path.exists() — path exist karta hai ya nahi
# - pathlib.Path — paths ke saath kaam karna
# - Path.name, Path.suffix, Path.parent
# - Path.is_file() aur Path.is_dir()

# Ek program banao jo:
# 1. Current working directory print kare.
# 2. Current folder ke items print kare.
# 3. Check kare ki practical3.py exist karti hai ya nahi.
# 4. File ka naam, extension aur parent folder print kare.
# 5. Check kare ki path file hai ya directory.
# 6. Saare results clearly print kare.

# Expected checks: file ka naam practical3.py, extension .py, aur is_file() ka result True hona chahiye, agar tum usi folder se program run kar rahe ho.

import os
from pathlib import Path

path = Path("practical3.py")
folder_items = os.listdir()

print("Current Working Directory:", os.getcwd())
print("\nItems in Current Directory:")
for item in folder_items:
    print(item)

print("\nChecking if 'practical3.py' exists:")
if os.path.exists(path):
    print("practical3.py exists.")
    print("File Name:", path.name)
    print("Extension:", path.suffix)
    print("Parent Folder:", path.parent)
    print("Is file?", path.is_file())
    print("Is directory?", path.is_dir())
else:
    print("practical3.py does not exist.")