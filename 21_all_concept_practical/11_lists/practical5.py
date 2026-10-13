# Task
# Ek function banao: def analyze_products(products)

# Products ki list:
products = [
    ["Laptop", 55000],
    ["Mouse", 800],
    ["Keyboard", 1500],
    ["Monitor", 12000]
]
# Function mein:
# 1. Agar list empty ho, to "No products available" return karo.
# 2. Sabhi product prices ki list banao.
# 3. Sabse mehenga aur sabse sasta product find karo.
# 4. sorted() aur key=lambda product: product[1] se products ko price ke ascending order mein sort karo.
# 5. ₹5,000 se zyada price wale products ki list comprehension se nayi list banao.
# 6. Ek dictionary return karo jisme cheapest, costliest, sorted_products aur above_5000 keys hon.
# 7. Function ko original list aur empty list, dono ke saath test karo.

# Expected output:
# {
#     'cheapest': ['Mouse', 800],
#     'costliest': ['Laptop', 55000],
#     'sorted_products': [
#         ['Mouse', 800],
#         ['Keyboard', 1500],
#         ['Monitor', 12000],
#         ['Laptop', 55000]
#     ],
#     'above_5000': [
#         ['Laptop', 55000],
#         ['Monitor', 12000]
#     ]
# }
# No products available


def analyze_products(products):
    if not products:
        return "No products available"
    
    cheapest = min(products, key = lambda x : x[1])
    costliest = max(products, key = lambda x : x[1])
    sorted_products = sorted(products, key = lambda x : x[1])
    above_5000 = list(filter(lambda x : x[1] > 5000, products))

    return {
        "cheapest": cheapest,
        "costliest": costliest,
        "sorted_products": sorted_products,
        "above_5000": above_5000
    }

print(analyze_products(products))
print(analyze_products([]))