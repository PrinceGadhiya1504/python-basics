# Function analyze_numbers(numbers) banao:
# 1. Empty tuple par "No numbers available" return karo.
# 2. len() se total elements count karo.
# 3. count() se 20 kitni baar aaya hai, nikalo.
# 4. index() se 40 ka pehla index nikalo.
# 5. sum(), min() aur max() se total, smallest aur largest values nikalo.
# 6. Slicing se tuple ke first 3 elements aur last 2 elements nikalo.
# 7. in operator se check karo ki 30 tuple mein hai ya nahi.
# 8. sorted() se ascending order mein values ki list banao.
# 9. set() se duplicate values remove karo.
# 10. Results dictionary mein return karo; normal aur empty tuple dono test karo.
# Expected output
# {
#     "total_elements": 7,
#     "count_20": 3,
#     "index_40": 4,
#     "total": 190,
#     "smallest": 10,
#     "largest": 50,
#     "first_three": (10, 20, 30),
#     "last_two": (20, 20),
#     "contains_30": True,
#     "sorted_numbers": [10, 20, 20, 20, 30, 40, 50],
#     "unique_numbers": {10, 20, 30, 40, 50}
# }
# No numbers available

numbers = (10, 20, 30, 20, 40, 50, 20)

def analyze_numbers(numbers):
    if not numbers:
        return "No numbers available"

    total_elements = len(numbers)
    count_20 = numbers.count(20)
    index_40 = numbers.index(40)
    total = sum(numbers)
    smallest = min(numbers)
    largest = max(numbers)
    first_three = numbers[:3]
    last_two = numbers[-2:]
    contains_30 = 30 in numbers
    sorted_numbers = sorted(numbers)
    unique_numbers = set(numbers)
    
    return {
        "total_elements": total_elements,
        "count_20": count_20,
        "index_40": index_40,
        "total": total,
        "smallest": smallest,
        "largest": largest,
        "first_three": first_three,
        "last_two": last_two,
        "contains_30": contains_30,
        "sorted_numbers": sorted_numbers,
        "unique_numbers": unique_numbers
    }

print(analyze_numbers(numbers))
print(analyze_numbers(()))