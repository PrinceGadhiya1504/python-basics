# Ek function process_number(value) banao jo:
# 1. try block mein int(value) kare.
# 2. Agar value integer mein convert nahi ho sakti, to ValueError handle kare aur "Invalid number" return kare.
# 3. Number ko 100 / number se divide kare.
# 4. Agar number 0 ho, to ZeroDivisionError handle kare aur "Cannot divide by zero" return kare.
# 5. Successful result ko else block se return kare.
# 6. finally mein "Processing completed" print kare.
# 7. In values ko test kare:

# Expected results:
# - "10" → 10.0
# - "abc" → "Invalid number"
# - "0" → "Cannot divide by zero"

def process_number(value):
    try:
        number = int(value)
        result = 100 / number
    except ValueError:
        return "Invalid number"
    except ZeroDivisionError:
        return "Cannot divide by zero"
    else:
        return result
    finally:
        print("Processing completed")


print(process_number("10"))
print(process_number("abc"))
print(process_number("0"))