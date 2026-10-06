# F-Strings
# F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.
# To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.

age = 23
txt = f"My name is Prince, I am {age} years old"
print(txt)

# Placeholders and Modifiers
# A placeholder can include a modifier to format the value.
# A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:

print(f"{age:.2f}")

#A placeholder can contain Python code, like math operations:
txt = f"The price is {20 * 10}"
print(txt)

#To insert a string with a sign, use the plus sign +:
price = 49
print(f"The price is {price:+d}")
