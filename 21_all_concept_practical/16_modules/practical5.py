# Ek program banao jo:
# 1. pathlib se student_data.txt ka path banaye.
# 2. datetime module se current date aur time nikale.
# 3. math module se 144 ka square root nikale.
# 4. os.path.exists() se check kare ki student_data.txt exist karti hai ya nahi.
# 5. try-except aur with open() se file read kare.
# 6. File missing ho to FileNotFoundError handle karke "Student file not found" print kare.
# 7. File exist karti ho to uska content print kare.
# 8. finally mein "Program execution completed" print kare.

# Static filename: student_data.txt

# Testing ke liye pehle file create kiye bina program run karna, taaki missing-file handling test ho. Phir file create karke dobara run karna.
# Expected checks:
# - Square root: 12.0
# - File missing ho to: Student file not found
# - Har case mein: Program execution completed

import os
import math
import datetime as dt
from pathlib import Path

def analyze_student_file():
    path = Path("student_data.txt")

    # Current date and time
    current_datetime = dt.datetime.now()
    print("Current Date and Time:", current_datetime)

    # Square root using math module
    square_root = math.sqrt(144)
    print("Square Root of 144:", square_root)

    # Check whether file exists
    print("File Exists:", os.path.exists(path))

    try:
        with open(path, "r") as file:
            content = file.read()

    except FileNotFoundError:
        print("Student file not found")

    else:
        print("Student File Content:")
        print(content)

    finally:
        print("Program execution completed")


analyze_student_file()