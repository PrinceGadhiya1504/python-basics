# Tumhe ek program banana hai jo:
# 1. calculate_total() function banaye, jo price × quantity calculate kare.
# 2. Har item ke liye total price dictionary me total key ke andar store kare.
# 3. try-except se invalid ya negative price/quantity handle kare.
# 4. Total price ₹1,000 ya usse zyada ho to 10% discount de, warna discount 0 ho.
# 5. filter() se ₹1,000 ya usse zyada total wale items select kare.
# 6. sorted() se items ko total price ke descending order me sort kare.
# 7. map() se har item ka message banaye, jaise "Laptop: ₹50000".
# 8. Sabhi valid items ka final bill calculate kare, discount minus karne ke baad.

cart = [
    {"name": "Laptop", "price": 50000, "quantity": 1},
    {"name": "Mouse", "price": 500, "quantity": 2},
    {"name": "Keyboard", "price": 1500, "quantity": 1},
    {"name": "USB Cable", "price": 200, "quantity": 3}
]

def calculate_total(item):
    price = item["price"]
    quantity = item["quantity"]

    # Validate price
    if type(price) not in (int, float):
        raise TypeError("Price must be a number")

    if price < 0:
        raise ValueError("Price cannot be negative")

    # Validate quantity
    if type(quantity) is not int:
        raise TypeError("Quantity must be an integer")

    if quantity < 0:
        raise ValueError("Quantity cannot be negative")

    return price * quantity


# Calculate total and discount for each item
for item in cart:
    try:
        item["total"] = calculate_total(item)

        if item["total"] >= 1000:
            item["discount"] = item["total"] * 0.10
        else:
            item["discount"] = 0

        item["final_price"] = item["total"] - item["discount"]

    except (TypeError, ValueError):
        item["total"] = "Invalid"
        item["discount"] = "Invalid"
        item["final_price"] = "Invalid"


# 1. Shopping Cart Report
print("Shopping Cart Report:")

for item in cart:
    print(
        f"Name: {item['name']}, "
        f"Price: {item['price']}, "
        f"Quantity: {item['quantity']}, "
        f"Total: {item['total']}, "
        f"Discount: {item['discount']}, "
        f"Final Price: {item['final_price']}"
    )


# 2. Items with total price >= 1000
print("\nItems with Total >= 1000:")

filtered_items = list(filter(lambda item: type(item["total"]) in (int, float)and item["total"] >= 1000,cart))

for item in filtered_items:
    print(f"{item['name']}: {item['total']}")


# 3. Sort items by total price (descending)
print("\nSorted Items by Total Price:")

valid_items = list(filter(lambda item: type(item["total"]) in (int, float),cart))

sorted_items = sorted(valid_items,key=lambda item: item["total"],reverse=True)

for item in sorted_items:
    print(f"{item['name']}: {item['total']}")


# 4. Create item messages using map()
print("\nItem Messages:")

messages = list(map(lambda item: f"{item['name']}: ₹{item['total']}",valid_items))
print(messages)


# 5. Calculate final bill after discounts
final_bill = sum(item["final_price"] for item in valid_items)

print("\nFinal Bill After Discount: ₹", final_bill)