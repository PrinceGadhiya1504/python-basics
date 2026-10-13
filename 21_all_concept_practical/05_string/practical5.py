# split() with a separator
# Comma-separated values
    # fruits = "apple,banana,mango" variable banao.
    # split() use karke comma , ke basis par string ko divide karo.
    # Result print karo.
    # Result ka data type print karo.

# Expected output:
    # ['apple', 'banana', 'mango']
    # <class 'list'>

fruits = "apple,banana,mango"
split_fruits = fruits.split(",")
print(split_fruits)
print(type(split_fruits))
