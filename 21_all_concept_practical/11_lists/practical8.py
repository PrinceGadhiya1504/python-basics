# Ek function analyze_inventory(products) banao jo:
# 1. Empty list hone par "Inventory is empty" return kare.
# 2. Total products ki count nikale.
# 3. Sabhi products ki total stock quantity nikale.
# 4. sum() se total inventory value calculate kare: price * stock.
# 5. sorted() aur lambda se products ko price ke descending order mein sort kare.
# 6. List comprehension se stock available (stock > 0) products nikale.
# 7. filter() se out-of-stock (stock == 0) products nikale.
# 8. Dictionary mein saare results return kare.
# 9. Normal aur empty list dono test kare.

# Expected results:

# Result	                         Expected value
# Total products	                 5
# Total stock	                     18
# Total inventory value	         ₹66,000
# Highest-priced product	         Monitor
# Available products	             Keyboard, Monitor, Headphones
# Out-of-stock products	         Mouse, Webcam

products = [
    {"name": "Keyboard", "price": 1200, "stock": 10},
    {"name": "Mouse", "price": 500, "stock": 0},
    {"name": "Monitor", "price": 8500, "stock": 5},
    {"name": "Headphones", "price": 2000, "stock": 3},
    {"name": "Webcam", "price": 3000, "stock": 0}
]

def analyze_inventory(products):
    if not products:
        return "Inventory is empty"

    total_products = len(products)
    total_stock = sum(product['stock'] for product in products)
    total_inventory_value = sum(product['price'] * product['stock'] for product in products)
    sorted_products = sorted(products, key=lambda x: x['price'], reverse=True)
    available_stock = [product for product in products if product['stock'] > 0]
    out_of_stock = list(filter(lambda x : x['stock'] == 0, products))

    return{
        "total_products": total_products,
        "total_stock": total_stock,
        "total_inventory_value": total_inventory_value,
        "sorted_products": sorted_products,
        "available_stock": available_stock,
        "out_of_stock": out_of_stock
    }

print(analyze_inventory(products))
print(analyze_inventory([]))