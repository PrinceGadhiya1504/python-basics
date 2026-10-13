# Ek function analyze_products(products) banao jo:
# 1. Empty tuple hone par "No products available" return kare.
# 2. len() se total records count kare.
# 3. count() se "Laptop" kitni baar aaya hai, count kare.
# 4. index() se pehle "Monitor" ka index nikale.
# 5. sum() se sabhi product prices ka total nikale.
# 6. max() aur min() se highest aur lowest price wale poore tuples nikale.
# 7. sorted() aur lambda se price ke descending order mein sort kare.
# 8. Set comprehension se unique categories nikale.
# 9. Saare results dictionary mein return kare.
# 10. Normal aur empty tuple dono test kare.

# Expected output
# {
#     "total_records": 6,
#     "laptop_count": 2,
#     "monitor_index": 4,
#     "total_price": 114500,
#     "highest_price_product": ("Laptop", 50000, "Electronics"),
#     "lowest_price_product": ("Mouse", 500, "Accessories"),
#     "sorted_products": [
#         ("Laptop", 50000, "Electronics"),
#         ("Laptop", 50000, "Electronics"),
#         ("Monitor", 12000, "Electronics"),
#         ("Keyboard", 1500, "Accessories"),
#         ("Mouse", 500, "Accessories"),
#         ("Mouse", 500, "Accessories")
#     ],
#     "unique_categories": {"Electronics", "Accessories"}
# }
# No products available

products = (
    ("Laptop", 50000, "Electronics"),
    ("Mouse", 500, "Accessories"),
    ("Laptop", 50000, "Electronics"),
    ("Keyboard", 1500, "Accessories"),
    ("Monitor", 12000, "Electronics"),
    ("Mouse", 500, "Accessories")
)

def analyze_products(products):
    if not products:
        return "No products available"

    total_record = len(products)
    laptop_count = sum(1 for product in products if product[0] == "Laptop")
    monitor_index = next(
        i for i, product in enumerate(products)
        if product[0] == "Monitor"
    )
    total_price = sum(product[1] for product in products)
    highest_price_product = max(products, key = lambda x : x[1])
    lowest_price_product = min(products, key = lambda x : x[1])
    sorted_products = sorted(products, key = lambda x : x[1], reverse=True)
    unique_categories = set(product[2] for product in products)

    return {
        "total_records": total_record,
        "laptop_count": laptop_count,
        "monitor_index": monitor_index,
        "total_price": total_price,
        "highest_price_product": highest_price_product,
        "lowest_price_product": lowest_price_product,
        "sorted_products": sorted_products,
        "unique_categories": unique_categories
    }

print(analyze_products(products))
print(analyze_products(()))