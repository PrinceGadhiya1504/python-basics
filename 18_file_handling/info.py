# File handling means working with files using Python.
# Using file handling, we can:
    # Create a file
    # Open a file
    # Read a file
    # Write data to a file
    # Append data to a file
    # Close a file
    # Delete a file

# 1. Why do we need File Handling?
# Variables store data temporarily while the program is running.
# Example:
name = "Prince"
age = 23

# When the program stops, these values are lost from memory.
# If we want to store data permanently, we can save it inside a file.

# 2. open() Function
# Python provides the open() function to work with files.
# Basic syntax:
    # open("filename", "mode")

file = open("data.txt", "r")
# "data.txt" -> file name
# "r"        -> read mode

# Always close a manually opened file:
file.close()

# 3. File Modes
    # r -> Read (Default mode)
    # w -> Write
    # a -> Append
    # x -> Create
    # b -> Binary
    # t -> Text (Default mode)

# Common combinations:
    # rb -> Read Binary
    # wb -> Write Binary
    # rt -> Read Text
    # wt -> Write Text

# 4. "r" - Read Mode
# It is used when we want to read the content of a file.
file = open("data.txt", "r")
content = file.read()
print(content)
file.close()

# Important:
# If the file does not exist, Python can raise: FileNotFoundError

# 5. read() Method
# read() reads the content of the file.
file = open("data.txt", "r")
content = file.read()
print(content)
file.close()
# read() normally reads the complete file.

# 6. read(number)
# We can provide a number to read() to specify
# how many characters we want to read.
file = open("data.txt", "r")
content = file.read(5)
print(content)
file.close()

# 7. readline()
# readline() reads one line at a time.
file = open("data.txt", "r")
line1 = file.readline() # First line
line2 = file.readline() # Second line
print(line1)
print(line2)
file.close()

# 8. readlines()
# readlines() reads all lines and returns them as a list.
file = open("data.txt", "r")
lines = file.readlines()
print(lines)
file.close()

# 9. Reading a File Using a for Loop
# We can directly loop through a file.
# This reads the file line by line.
file = open("data.txt", "r")
for line in file:
    print(line)
file.close()
# This approach is useful when working with
# multiple lines or large files.

# 10. "w" - Write Mode
# It is used to write data into a file.
file = open("new_file.txt", "w")
file.write("Hello Prince")
file.close()
# If the file does not exist: Python creates the file.
# If the file already exists: All previous content is deleted.
# The file is overwritten.
# Suppose new_file.txt contains:
    # Hello
    # Welcome
# Now:
file = open("data.txt", "w")
file.write("Python")
file.close()
# The old content is replaced.
# File now contains:
# Python

# 12. "a" - Append Mode
# Add new data at the end of the existing data.
# Existing data is not removed.
file = open("data.txt", "a")
file.write("\nWelcome to Python")
file.close()

# 13. "w" vs "a"
# "w" -> replaces existing content
# "a" -> keeps existing content and adds new content

# 14. "x" - Create Mode
# It creates a new file.
# If the file already exists, Python raises: FileExistsError
file = open("new_file.txt", "x")
file.close()
# The file is created if it does not already exist.

# 15. "b" - Binary Mode
# Binary mode is used when working with binary data.
# Examples:
    # - Images
    # - Videos
    # - Audio
    # - PDF files
file = open("image.jpg", "rb")
data = file.read()
file.close()

# 16. "t" - Text Mode
# Text mode is normally the default mode.
file = open("data.txt", "rt")
content = file.read()
print(content)
file.close()
# "r" and "rt" are normally used for reading text.

# 17. close() Method
# When we manually use open(), we should close the file after finishing our work.
file = open("data.txt", "r")
content = file.read()
print(content)
file.close()

# Why close the file?
    # Releases the file resource.
    # Prevents unnecessary resource usage.
    # Ensures the file is properly closed.

# 18. with open()
# Python provides a better and safer way to work with files:
# Example:
with open("data.txt", "r") as file:
    content = file.read()
    print(content)
# We do NOT need to call file.close() manually.
# Python automatically closes the file when the "with" block finishes.

# 19. Why use with open()?
# Recommended approach:
with open("data.txt", "r") as file:
    content = file.read()
# It automatically handles closing the file.
# Therefore, it is generally better than manually:
# file = open(...)
# ...
# file.close()

# 20. Writing with with open()
with open("data.txt", "w") as file:
    file.write("Hello Prince")
# The file is automatically closed after the block.

# 21. Appending with with open()
with open("data.txt", "a") as file:
    file.write("\nPython is easy")
# Existing content is preserved and new content is added.

# 22. Reading and Writing Multiple Lines
students = [
    "Prince\n",
    "Rahul\n",
    "Amit\n"
]

with open("students.txt", "w") as file:
    file.writelines(students)
# students.txt will contain:
# Prince
# Rahul
# Amit


# 23. writelines()
# writelines() writes multiple strings to a file.
# IMPORTANT: writelines() does NOT automatically add a newline.
# Therefore, if we want each value on a new line, we should include "\n" ourselves.
students = [
    "Prince\n",
    "Rahul\n",
    "Amit\n"
]

with open("students.txt", "w") as file:
    file.writelines(students)

# 24. File Existence Check
# We can use the os module to check whether a file exists.
import os
if os.path.exists("data.txt"):
    print("File exists")
else:
    print("File does not exist")

# 25. Delete a File
# We can use os.remove() to delete a file.
import os
if os.path.exists("data.txt"):
    os.remove("data.txt")
    print("File deleted")
else:
    print("File does not exist")

# 26. Remove an Empty Folder
# os.rmdir() can remove an empty directory.
# If any file exist then it will give error
import os
if os.path.exists("myfolder"):
    os.rmdir("myfolder")
    print("Folder deleted")
# IMPORTANT: os.rmdir() is used for an empty directory.

# 27. FileNotFoundError
# If we try to open a file that does not exist in read mode, Python can raise FileNotFoundError.
try:
    with open("not_found.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File does not exist")
# Output:
# File does not exist

# 28. File Handling with User Input
# We can take input from the user and save it into a file.
name = input("Enter your name: ")
with open("users.txt", "a") as file:
    file.write(name + "\n")
print("Name saved successfully")

# Let's save multiple student names.
students = ["Prince", "Rahul", "Amit"]
with open("students.txt", "w") as file:
    for student in students:
        file.write(student + "\n")
# Now students.txt contains:
# Prince
# Rahul
# Amit

# Read Student Data
with open("students.txt", "r") as file:
    for student in file:
        print(student.strip())
# strip() removes extra whitespace/newline characters.

# 29. Read + Process Data
with open("students.txt", "r") as file:
    for student in file:
        student = student.strip()
        print("Student: ", student)
# Example output:
# Student: Prince
# Student: Rahul
# Student: Amit

# 30. File Position - tell()
# tell() returns the current position of the file cursor.
with open("data.txt", "r") as file:
    print(file.tell())
# Initially, the position is normally:
# 0
# After reading some data, the position changes.

# 31. File Position - seek()
# seek() changes the current position of the file cursor.
with open("data.txt", "r") as file:
    file.seek(0)
    content = file.read()
    print(content)
# seek(0) moves the cursor back to the beginning.

# 32. Encoding
# When working with text files, we can specify an encoding.
# UTF-8 is commonly used.
with open("data.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)
# When writing:
with open("data.txt", "w", encoding="utf-8") as file:
    file.write("Hello Prince")
# Specifying encoding can help when working with non-English characters.

# 33. File Handling + Exception Handling
try:
    with(open("data.txt", "r")) as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File does not exist")
except PermissionError:
    print("You do not have permission to access the file")
except OSError:
    print("Some operating system error occurred")

# 34. Important File Methods
# open()
# -> Opens a file.

# read()
# -> Reads file content.

# readline()
# -> Reads one line.

# readlines()
# -> Reads all lines and returns a list.

# write()
# -> Writes data to a file.

# writelines()
# -> Writes multiple strings.

# close()
# -> Closes the file.

# tell()
# -> Returns current file position.

# seek()
# -> Changes file position.

