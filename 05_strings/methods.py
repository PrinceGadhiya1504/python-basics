# 1. capitalize()
# Converts the first character to upper case
# and the remaining characters to lower case.

txt = "hello PYTHON DEVELOPER"
print("#1 capitalize :", txt.capitalize())

txt = "23 is my Age."
print("#1 capitalize :", txt.capitalize())


# 2. casefold()
# Converts a string into a case-insensitive lowercase form.

txt = "My NAME is PRINCE"
print("#2 casefold :", txt.casefold())


# 3. center()
# Returns a centered string.

txt = "Apple"
print("#3 center :", txt.center(20))
print("#3 center length :", len(txt.center(20)))

# center() with custom character
print("#3 center custom :", txt.center(20, "-"))


# 4. count()
# Returns the number of times a specified value occurs.

txt = "apple apple banana apple"

print("#4 count apple :", txt.count("apple"))
print("#4 count banana :", txt.count("banana"))
print("#4 count mango :", txt.count("mango"))


# 5. encode()
# Converts the string into bytes using an encoding.
# UTF-8 is the default encoding.

txt = "Hello World"
print("#5 encode :", txt.encode())

txt = "Héllo Wörld"
print("#5 encode :", txt.encode())


# 6. endswith()
# Returns True if the string ends with the specified value.
# Otherwise False.

txt = "Hello, welcome to my world."

print("#6 endswith True :", txt.endswith("world."))
print("#6 endswith False :", txt.endswith("Python"))


# 7. find()
# Searches for a value and returns its first position.
# Returns -1 if value is not found.

txt = "Hello, welcome to my world."

print("#7 find welcome :", txt.find("welcome"))
print("#7 find e :", txt.find("e"))

# Search between position 5 and 10
print("#7 find e 5-10 :", txt.find("e", 5, 10))

# Value not found
print("#7 find q :", txt.find("q"))


# 8. format()
# Inserts values into placeholders {}.

txt1 = "My name is {fname}, I'm {age}".format(fname="Prince", age=23)
txt2 = "My name is {0}, I'm {1}".format("Prince", 23)
txt3 = "My name is {}, I'm {}".format("Prince",23)

print("#8 format 1 :", txt1)
print("#8 format 2 :", txt2)
print("#8 format 3 :", txt3)


# 9. index()
# Searches for a value and returns its first position.
# Raises ValueError if value is not found.

txt = "Hello, welcome to my world."

print("#9 index welcome :", txt.index("welcome"))
print("#9 index e :", txt.index("e"))

# Don't run this unless you want to see the error:
# print(txt.index("q"))

# Difference:
# find("q")  -> -1
# index("q") -> ValueError


# 10. isalnum()
# Returns True if all characters are letters or numbers.
# Spaces and special characters make it False.

txt1 = "Company12"
txt2 = "Company123"
txt3 = "Company 12"
txt4 = "Company-12"

print("#10 isalnum True  :", txt1.isalnum())
print("#10 isalnum True  :", txt2.isalnum())
print("#10 isalnum False :", txt3.isalnum())
print("#10 isalnum False :", txt4.isalnum())


# 11. isalpha()
# Returns True if all characters are alphabetic.

txt1 = "Company"
txt2 = "Company12"
txt3 = "Company Name"

print("#11 isalpha True  :", txt1.isalpha())
print("#11 isalpha False :", txt2.isalpha())
print("#11 isalpha False :", txt3.isalpha())


# 12. isascii()
# Returns True if all characters are ASCII characters.
# ASCII includes common English letters, digits and symbols.

txt1 = "Hello World"
txt2 = "Hello#World"
txt3 = "Héllo"

print("#12 isascii True  :", txt1.isascii())
print("#12 isascii True  :", txt2.isascii())
print("#12 isascii False :", txt3.isascii())


# 13. isdecimal()
# Returns True if all characters are decimal characters.

txt1 = "23"
txt2 = "12345"
txt3 = "23²"
txt4 = "23.5"

print("#13 isdecimal True  :", txt1.isdecimal())
print("#13 isdecimal True  :", txt2.isdecimal())
print("#13 isdecimal False :", txt3.isdecimal())
print("#13 isdecimal False :", txt4.isdecimal())


# 14. isdigit()
# Returns True if all characters are digits.

txt1 = "23"
txt2 = "12345"
txt3 = "23²"
txt4 = "23.5"

print("#14 isdigit True  :", txt1.isdigit())
print("#14 isdigit True  :", txt2.isdigit())
print("#14 isdigit True  :", txt3.isdigit())
print("#14 isdigit False :", txt4.isdigit())


# 15. isidentifier()
# Returns True if the string is a valid Python identifier.
# A string is considered a valid identifier if:
# 1.it only contains alphanumeric letters (a-z) and (0-9), or underscores (_). 
# 2. A valid identifier cannot start with a number, or contain any spaces.

txt1 = "MyVariable"
txt2 = "My_Variable"
txt3 = "MyVariable123"
txt4 = "123Variable"
txt5 = "My-Variable"
txt6 = "My Variable"

print("#15 isidentifier True  :", txt1.isidentifier())
print("#15 isidentifier True  :", txt2.isidentifier())
print("#15 isidentifier True  :", txt3.isidentifier())
print("#15 isidentifier False :", txt4.isidentifier())
print("#15 isidentifier False :", txt5.isidentifier())
print("#15 isidentifier False :", txt6.isidentifier())


# 16. islower()
# Returns True if all cased characters are lowercase.

txt1 = "python"
txt2 = "Python"
txt3 = "PYTHON"
txt4 = "python developer"

print("#16 islower True  :", txt1.islower())
print("#16 islower False :", txt2.islower())
print("#16 islower False :", txt3.islower())
print("#16 islower True  :", txt4.islower())


# 17. isnumeric()
# Returns True if all characters are numeric.
# The isnumeric() method returns True if all the characters are numeric (0-9), otherwise False.
# Exponents, like ² and ¾ are also considered to be numeric values.
# "-1" and "1.5" are NOT considered numeric values, because all the characters in the string must be numeric, and the - and the . are not.

txt1 = "23"
txt2 = "12345"
txt3 = "-23"
txt4 = "23.5"
txt5 = "⅕"

print("#17 isnumeric True  :", txt1.isnumeric())
print("#17 isnumeric True  :", txt2.isnumeric())
print("#17 isnumeric False :", txt3.isnumeric())
print("#17 isnumeric False :", txt4.isnumeric())
print("#17 isnumeric True  :", txt5.isnumeric())


# 18. isprintable()
# Returns True if all characters are printable.

txt1 = "Hello World"
txt2 = "Hello\nWorld"
txt3 = "Hello\tWorld"

print("#18 isprintable True  :", txt1.isprintable())
print("#18 isprintable False :", txt2.isprintable())
print("#18 isprintable False :", txt3.isprintable())


# 19. isspace()
# Returns True if all characters are whitespace
# and there is at least one character.

txt1 = " "
txt2 = "   "
txt3 = "\t"
txt4 = "Hello"

print("#19 isspace True  :", txt1.isspace())
print("#19 isspace True  :", txt2.isspace())
print("#19 isspace True  :", txt3.isspace())
print("#19 isspace False :", txt4.isspace())

# Empty string is False
print("#19 isspace empty :", "".isspace())


# 20. istitle()
# Returns True if the string follows title-case rules.

txt1 = "Hello World"
txt2 = "Python Developer"
txt3 = "hello world"
txt4 = "HELLO WORLD"

print("#20 istitle True  :", txt1.istitle())
print("#20 istitle True  :", txt2.istitle())
print("#20 istitle False :", txt3.istitle())
print("#20 istitle False :", txt4.istitle())


# 21. isupper()
# Returns True if all cased characters are uppercase.

txt1 = "PYTHON"
txt2 = "Python"
txt3 = "python"
txt4 = "PYTHON DEVELOPER"

print("#21 isupper True  :", txt1.isupper())
print("#21 isupper False :", txt2.isupper())
print("#21 isupper False :", txt3.isupper())
print("#21 isupper True  :", txt4.isupper())


# 22. join()
# Joins elements of an iterable using the string as separator.

words = ["Python", "is", "easy"]

print("#22 join space :", " ".join(words))
print("#22 join dash  :", "-".join(words))
print("#22 join comma :", ", ".join(words))


# 23. ljust()
# Returns a left-justified string.

txt = "Apple"

print("#23 ljust :", txt.ljust(10))
print("#23 ljust custom :", txt.ljust(10, "-"))


# 24. lower()
# Converts a string to lowercase.

txt1 = "PYTHON DEVELOPER"
txt2 = "Hello World"

print("#24 lower :", txt1.lower())
print("#24 lower :", txt2.lower())


# 25. lstrip()
# Removes whitespace from the left side.

txt = "     Hello World"

print("#25 lstrip :", txt.lstrip())

# Custom character removal
txt = ".....Hello World"
print("#25 lstrip custom :", txt.lstrip("."))


# 26. maketrans()
# Creates a translation table used with translate().

txt = "hello world"

translation_table = str.maketrans(
    "hw",
    "HW"
)

print("#26 maketrans :", txt.translate(translation_table))


# 27. partition()
# Splits the string into three parts:
# before separator, separator, after separator.

txt = "I love Python"

print("#27 partition :", txt.partition("love"))
print("#27 partition :", txt.partition("Java"))


# 28. replace()
# Replaces a specified value with another value.

txt = "I love Java"

print("#28 replace :", txt.replace("Java", "Python"))

txt = "apple apple apple"

print("#28 replace all :", txt.replace("apple", "banana"))

# Replace only first 1 occurrence
print("#28 replace one :", txt.replace("apple", "banana", 1))


# 29. rfind()
# Searches from the right and returns the last position.

txt = "Python is easy and Python is powerful"

print("#29 rfind :", txt.rfind("Python"))
print("#29 rfind not found :", txt.rfind("Java"))


# 30. rindex()
# Searches from the right and returns the last position.
# Raises ValueError if not found.

txt = "Python is easy and Python is powerful"

print("#30 rindex :", txt.rindex("Python"))

# Don't run unless you want to see the error:
# print(txt.rindex("Java"))


# 31. rjust()
# Returns a right-justified string.

txt = "Apple"

print("#31 rjust :", txt.rjust(10))
print("#31 rjust custom :", txt.rjust(10, "-"))


# 32. rpartition()
# Searches for the last occurrence of separator
# and returns three parts.

txt = "Python is easy and Python is powerful"

print("#32 rpartition :", txt.rpartition("Python"))
print("#32 rpartition :", txt.rpartition("Java"))


# 33. rsplit()
# Splits the string from the right.

txt = "apple,banana,orange"

print("#33 rsplit :", txt.rsplit(","))

# maxsplit = 1
print("#33 rsplit max 1 :", txt.rsplit(",", 1))


# 34. rstrip()
# Removes whitespace from the right side.

txt = "Hello World     "

print("#34 rstrip :", txt.rstrip())

# Custom character removal
txt = "Hello World....."

print("#34 rstrip custom :", txt.rstrip("."))


# 35. split()
# Splits a string and returns a list.

txt = "Python is easy"

print("#35 split :", txt.split())

txt = "apple,banana,orange"

print("#35 split comma :", txt.split(","))


# 36. splitlines()
# Splits a string at line breaks.

txt = "Hello\nWorld\nPython"

print("#36 splitlines :", txt.splitlines())


# 37. startswith()
# Returns True if the string starts with specified value.

txt = "Hello, welcome to Python."

print("#37 startswith True  :", txt.startswith("Hello"))
print("#37 startswith False :", txt.startswith("Python"))


# 38. strip()
# Removes whitespace from both left and right sides.

txt = "     Hello World     "

print("#38 strip :", txt.strip())

# Custom characters
txt = ".....Hello World....."

print("#38 strip custom :", txt.strip("."))


# 39. swapcase()
# Converts uppercase to lowercase and lowercase to uppercase.

txt = "Hello Python"

print("#39 swapcase :", txt.swapcase())


# 40. title()
# Converts the first character of each word to uppercase.

txt = "hello python developer"

print("#40 title :", txt.title())

txt = "my name is prince"

print("#40 title :", txt.title())


# 41. translate()
# Replaces characters according to a translation table.

txt = "hello world"

translation_table = str.maketrans(
    "hw",
    "HW"
)

print("#41 translate :", txt.translate(translation_table))


# 42. upper()
# Converts a string to uppercase.

txt1 = "python developer"
txt2 = "hello world"

print("#42 upper :", txt1.upper())
print("#42 upper :", txt2.upper())


# 43. zfill()
# Adds zeros to the beginning of a string
# until it reaches the specified width.

txt = "42"

print("#43 zfill :", txt.zfill(5))

txt = "123"

print("#43 zfill :", txt.zfill(6))

# zfill also handles signs
txt = "-42"

print("#43 zfill negative :", txt.zfill(5))