# Ek function calculate_division(a, b) banao jo:
# 1. try block mein a / b calculate kare.
# 2. ZeroDivisionError ko except se handle kare.
# 3. Division successful ho to result return kare.
# 4. Error aane par "Cannot divide by zero" return kare.
# 5. else ka use karke successful division ka message print kare.
# 6. finally ka use karke "Division operation completed" print kare.
# 7. Function ko in teen cases ke saath test kare:
#    - calculate_division(10, 2)
#    - calculate_division(10, 0)
#    - calculate_division(25, 5)
# Expected results:
# - 10 / 2 → 5.0
# - 10 / 0 → "Cannot divide by zero"
# - 25 / 5 → 5.0

def calculate_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    else:
        print("Division is successful")
        return result
    finally:
        print("Division operation completed")


print(calculate_division(10, 2))
print(calculate_division(10, 0))
print(calculate_division(25, 5))
