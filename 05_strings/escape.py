# To insert characters that are illegal in a string, use an escape character.
# An escape character is a backslash \ followed by the character you want to insert.

# You will get an error if you use double quotes inside a string that is surrounded by double quotes
# txt = "You are a "Python" developer
# To fix this problem, use the escape character \"
txt1 = "You are a \"Python\" developer"
print(txt1)

# \'   Insert a single quote
txt2 = 'It\'s my book'
print(txt2)

# \"   Insert a double quote
txt3 = "He said \"Hello\""
print(txt3)

# \\   Insert a backslash
txt4 = "C:\\Users\\Dellon"
print(txt4)

# \n   New Line
txt5 = "Hello\nNew Line"
print(txt5)

# \r  Return (carriage return)
txt6 = "Hello\rCarriage Return"
print(txt6)

# \t  Tab  
txt7 = "Hello\tTab"
print(txt7)

# \b  Backspace  
txt8 = "Hello\bWorld"
print(txt8)

# \f  Form Feed  
txt9 = "Hello\fForm Feed"
print(txt9)

# \ooo Octal value  
txt10 = "Hello\1770o0Octal"
print(txt10)

# \xhh Hex value
txt11 = "Hello\x77Hex"
print(txt11)