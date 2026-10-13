# Function analyze_sales(sales) banao jo:
# 1. sum() se total units sold nikale.
# 2. max() aur min() se highest aur lowest sales wale products nikale.
# 3. sorted() se products ko sales ke descending order mein sort kare.
# 4. reversed() se product names ka reverse order nikale.
# 5. Dictionary comprehension se sirf un products ka dictionary banaye jinki sales 10 ya zyada hain.
# 6. any() check kare ki koi product 15 se zyada units bech raha hai ya nahi.
# 7. all() check kare ki saare products ki sales 5 ya zyada hain ya nahi.
# 8. enumerate() se products ko numbering ke saath list mein store kare.
# 9. copy() se dictionary ki copy banaye aur usmein "Tablet": 7 add kare.
# 10. Saare results dictionary mein return kare.
# Expected checks:
# - Total units: 60
# - Highest sales product: "Mouse" — 20
# - Lowest sales product: "Laptop" — 5
# - any() → True
# - all() → True

sales = {
    "Laptop": 5,
    "Mouse": 20,
    "Keyboard": 12,
    "Monitor": 8,
    "Webcam": 15
}

def analyze_sales(sales):
    total_units = sum(sales.values())
    highest_product = max(sales, key=sales.get)
    lowest_product = min(sales, key=sales.get)
    sorted_products = sorted(sales.items(), key=lambda x: x[1], reverse=True)
    reversed_products = list(reversed(sales.keys()))
    products_10_plus = {product: sales[product] for product in sales if sales[product] >= 10}
    any_15_plus = any(sales[product] > 15 for product in sales)
    all_5_plus = all(sales[product] >= 5 for product in sales)
    enumerated_products = list(enumerate(sales.keys()))
    copy_sales = sales.copy()
    copy_sales["Tablet"] = 7

    return {
        "total_units": total_units,
        "highest_product": highest_product,
        "lowest_product": lowest_product,
        "sorted_products": sorted_products,
        "reversed_products": reversed_products,
        "products_10_plus": products_10_plus,
        "any_15_plus": any_15_plus,
        "all_5_plus": all_5_plus,
        "enumerated_products": enumerated_products,
        "copy_sales": copy_sales
    }
    
print(analyze_sales(sales))