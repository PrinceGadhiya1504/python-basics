# Task
# Ek analyze_numbers(*args, **kwargs) function banao:
    # 1. *args se numbers accept karo.
    # 2. filter() aur lambda se positive numbers select karo.
    # 3. map() aur lambda se unka square nikalo.
    # 4. try-except se empty input ko handle karo.
    # 5. **kwargs se ek operation keyword accept karo, jiska default "square" ho.
    # 6. Agar operation "square" hai, to positive numbers ke squares return karo.
    # 7. Agar operation "count" hai, to positive numbers ki total count return karo.
    # 8. Agar operation invalid hai, to "Invalid operation" return karo.
# Expected test cases:

# Function call	                                Expected output
# analyze_numbers(-2, 3, 4, -5, 6)	            [9, 16, 36]
# analyze_numbers(-2, 3, 4, operation="count")  2
# analyze_numbers(operation="square")	        []
# analyze_numbers(2, 3, operation="cube")	    Invalid operation

def analyze_numbers(*args,**kwargs):
    positive_numbers = list(filter(lambda x : x > 0, args))
    squared_numbers = list(map(lambda x : x * x, positive_numbers))
    operation = kwargs.get("operation", "square")
    try:
        if operation == "square":
            return squared_numbers
        elif operation == "count":
            return len(positive_numbers)
        else:
            return "Invalid operation"
    except TypeError:
        return "Invalid input"

print(analyze_numbers(-2, 3, 4, -5, 6))
print(analyze_numbers(-2, 3, 4, operation="count"))
print(analyze_numbers(operation="square"))
print(analyze_numbers(2, 3, operation="cube"))


