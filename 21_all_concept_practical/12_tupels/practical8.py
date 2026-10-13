# Ek function process_products(product_names, prices) banao:
# 1. Agar koi tuple empty ho ya lengths alag hon, toh "Invalid product data" return karo.
# 2. zip() se (product_name, price) ke tuples banao.
# 3. enumerate() se products ko 1 se numbering do.
# 4. sum() se total price nikalo.
# 5. max() aur min() se highest aur lowest price wale poore tuples nikalo.
# 6. filter() se ₹5,000 ya usse zyada price wale poore product tuples nikalo.
# 7. sorted() aur lambda se descending price order mein sort karo.
# 8. Product records ko list() se list mein convert karo.
# 9. any() se check karo ki koi product ₹40,000 se mehenga hai.
# 10. Sabhi results dictionary mein return karo.
# Expected output
# {
#     "product_records": (
#         ("Laptop", 50000),
#         ("Mouse", 500),
#         ("Keyboard", 1500),
#         ("Monitor", 12000),
#         ("Webcam", 3000)
#     ),
#     "numbered_products": [
#         (1, ("Laptop", 50000)),
#         (2, ("Mouse", 500)),
#         (3, ("Keyboard", 1500)),
#         (4, ("Monitor", 12000)),
#         (5, ("Webcam", 3000))
#     ],
#     "total_price": 67000,
#     "highest_price_product": ("Laptop", 50000),
#     "lowest_price_product": ("Mouse", 500),
#     "products_5000_plus": [
#         ("Laptop", 50000),
#         ("Monitor", 12000)
#     ],
#     "sorted_products": [
#         ("Laptop", 50000),
#         ("Monitor", 12000),
#         ("Webcam", 3000),
#         ("Keyboard", 1500),
#         ("Mouse", 500)
#     ],
#     "products_list": [
#         ("Laptop", 50000),
#         ("Mouse", 500),
#         ("Keyboard", 1500),
#         ("Monitor", 12000),
#         ("Webcam", 3000)
#     ],
#     "any_above_40000": True
# }

product_names = ("Laptop", "Mouse", "Keyboard", "Monitor", "Webcam")
prices = (50000, 500, 1500, 12000, 3000)

def process_products(product_names, prices):
    if not product_names or not prices or len(product_names) != len(prices):
        return "Invalid product data"
    
    product_records = tuple(zip(product_names, prices))
    numbered_products = list(enumerate(product_records, start=1))
    total_price = sum(prices)
    highest_price_product = max(product_records, key=lambda x: x[1])
    lowest_price_product = min(product_records, key=lambda x: x[1])
    products_5000_plus = list(filter(lambda x: x[1] >= 5000, product_records))
    sorted_products = sorted(product_records, key=lambda x: x[1], reverse=True)
    products_list = list(product_records)
    any_above_40000 = any(price >= 40000 for price in prices)
    
    return {
        "product_records": product_records,
        "numbered_products": numbered_products,
        "total_price": total_price,
        "highest_price_product": highest_price_product,
        "lowest_price_product": lowest_price_product,
        "products_5000_plus": products_5000_plus,
        "sorted_products": sorted_products,
        "products_list": products_list,
        "any_above_40000": any_above_40000
    }

print(process_products(product_names, prices))