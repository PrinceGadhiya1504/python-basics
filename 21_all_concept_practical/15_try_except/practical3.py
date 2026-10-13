# Ek function validate_age(age) banao jo:
# 1. Agar age integer nahi hai, to TypeError raise kare.
# 2. Agar age 0 ya negative hai, to ValueError raise kare.
# 3. Agar age 18 se kam hai, to "Not eligible" return kare.
# 4. Agar age 18 ya zyada hai, to "Eligible" return kare.
# 5. try-except se errors handle kare.
# 6. finally mein "Age validation completed" print kare.

# Expected results:
# - 21 → "Eligible"
# - 16 → "Not eligible"
# - 0 → "Age must be positive"
# - "twenty" → "Age must be an integer"

def validate_age(age):
    try:
        if type(age) is not int:
            raise TypeError
        if age <= 0:
            raise ValueError
        if age < 18:
            return "Not eligible"
        else:
            return "Eligible"
    except TypeError:
        return "Age must be an integer"
    except ValueError:
        return "Age must be positive"
    finally:
        print("Age validation completed")


print(validate_age(21))
print(validate_age(16))
print(validate_age(0))
print(validate_age("twenty"))
            