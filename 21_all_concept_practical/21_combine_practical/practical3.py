# Tasks:
# 1. get_stock_status() function banao:
#    - Stock 0 ho → "Out of Stock"
#    - Stock 1–5 ho → "Low Stock"
#    - Stock 5 se zyada ho → "Available"
# 2. Har product ke dictionary me status key add karo.
# 3. try-except se invalid price ya stock values handle karo. Price aur stock negative nahi hone chahiye.
# 4. Loop se product name, price, stock aur status print karo.
# 5. filter() se available products nikalo, jinka stock 0 se zyada ho.
# 6. sorted() aur lambda se products ko price ke descending order me sort karo.
# 7. Har product ka inventory value (price × stock) calculate karke print karo.

products = [
    {"name": "Laptop", "price": 50000, "stock": 5},
    {"name": "Mouse", "price": 500, "stock": 0},
    {"name": "Keyboard", "price": 1500, "stock": 10},
    {"name": "Monitor", "price": 12000, "stock": 3},
    {"name": "USB Cable", "price": 200, "stock": 20}
]

def get_stock_status(product):
    price = product["price"]
    stock = product["stock"]

    # Validate price
    if type(price) not in (int, float):
        raise TypeError("Price must be a number")

    if price < 0:
        raise ValueError("Price cannot be negative")

    # Validate stock
    if type(stock) is not int:
        raise TypeError("Stock must be an integer")

    if stock < 0:
        raise ValueError("Stock cannot be negative")

    # Determine stock status
    if stock == 0:
        return "Out of Stock"
    elif stock <= 5:
        return "Low Stock"
    else:
        return "Available"


# Calculate status and handle invalid data
for product in products:
    try:
        product["status"] = get_stock_status(product)
    except (TypeError, ValueError):
        product["status"] = "Invalid"


# 1. Product Report
print("Product Report:")

for product in products:
    print(
        f"Name: {product['name']}, "
        f"Price: {product['price']}, "
        f"Stock: {product['stock']}, "
        f"Status: {product['status']}"
    )


# 2. Available Products
available_products = list(filter(lambda p: p["stock"] > 0, products))

print("\nAvailable Products:")

for product in available_products:
    print(
        f"Name: {product['name']}, "
        f"Price: {product['price']}, "
        f"Stock: {product['stock']}"
    )


# 3. Sort valid products by price (descending)
valid_products = list(filter(lambda p: p["status"] != "Invalid", products))

sorted_products = sorted(valid_products,key=lambda p: p["price"], reverse=True)

print("\nSorted Products by Price:")

for product in sorted_products:
    print(
        f"Name: {product['name']}, "
        f"Price: {product['price']}, "
        f"Status: {product['status']}"
    )


# 4. Inventory Value = Price × Stock
print("\nInventory Value:")

for product in valid_products:
    inventory_value = product["price"] * product["stock"]

    print(
        f"Name: {product['name']}, "
        f"Inventory Value: {inventory_value}"
    )