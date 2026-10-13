# Ek function analyze_iterator(numbers) banao jo:
# 1. iter() se list ka iterator banaye.
# 2. next() se pehle 3 elements ek-ek karke nikale.
# 3. for loop se original list ke saare elements print kare.
# 4. Iterator ko list() mein convert karke uske remaining elements ki list nikale.
# 5. Ek empty iterator banaye aur next() call karne par aane wale StopIteration exception ko try-except se handle kare.
# 6. Results ko dictionary mein return kare.
# Important: Jab tum next() se 3 elements nikal loge, iterator un elements ko yaad rakhega ki woh consume ho chuke hain. Isliye remaining list mein sirf bache hue elements aayenge.
# Expected checks
# - First 3 elements: [10, 20, 30]
# - Remaining elements: [40, 50]
# - Empty iterator par: "Iterator is exhausted"

numbers = [10, 20, 30, 40, 50]

def analyze_iterator(numbers):
    iterator = iter(numbers)

    first_3_elements = [
        next(iterator),
        next(iterator),
        next(iterator)
    ]
    remaining_list = list(iterator)

    for i in iterator:
        print(i)

    empty_iterator = iter([])
    empty_iterator_result = None
    try:
        next(empty_iterator)
    except StopIteration:
        empty_iterator_result = "Iterator is exhausted"

    return {
        "first_3_elements": first_3_elements,
        "remaining_elements": remaining_list,
        "empty_iterator_check": empty_iterator_result
    }

print(analyze_iterator(numbers))