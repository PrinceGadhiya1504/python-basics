# String operations
    # first_name = "Prince" banao.
    # last_name = "Gadhiya" banao.
    # Dono strings ko jodkar full_name banao.
    # full_name ko uppercase aur lowercase mein print karo.
    # full_name ki length print karo.

# Expected output:
    # Full Name: Prince Gadhiya
    # Uppercase: PRINCE GADHIYA
    # Lowercase: prince gadhiya
    # Length: 14

first_name = "Prince"
last_name = "Gadhiya"

full_name = f"{first_name} {last_name}" # Method 1
# full_name = first_name + " " + last_name # Method 2
# full_name = "{} {}".format(first_name, last_name) # Method 3
# full_name = "%s %s" % (first_name, last_name) # Method 4

print("Full Name:", full_name)
print("Uppercase:", full_name.upper())
print("Lowercase:", full_name.lower())
print("Length:", len(full_name))