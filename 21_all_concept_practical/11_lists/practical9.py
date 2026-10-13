# analyze_sales(sales) naam ka function banao.
# 1. Empty list hone par "No sales data available" return karo.
# 2. Total products ki count nikalo.
# 3. Har product ki sales value (quantity × price) calculate karke total revenue nikalo.
# 4. max() se highest revenue generate karne wala product nikalo.
# 5. sorted() aur lambda se products ko revenue ke descending order mein sort karo.
# 6. List comprehension se un products ko nikalo jinki revenue ₹5,000 ya usse zyada hai.
# 7. filter() se un products ko nikalo jinki quantity 5 ya usse zyada hai.
# 8. Saare results ek dictionary mein return karo.
# 9. Normal aur empty list dono test karo.

# Expected results:
# Result	                    Expected value
# Total products	            5
# Total revenue	                ₹1,20,500
# Highest revenue	            Laptop — ₹90,000
# Revenue ₹5,000+	            Laptop, Monitor
# Quantity 5+	                Mouse, Keyboard


sales = [
    {"name": "Laptop", "price": 90000, "quantity": 1},
    {"name": "Mouse", "price": 500, "quantity": 10},
    {"name": "Keyboard", "price": 1200, "quantity": 8},
    {"name": "Monitor", "price": 12000, "quantity": 2},
    {"name": "Webcam", "price": 3000, "quantity": 5}
]

def analyze_sales(sales):
    if not sales:
        return "No sales data available"

    total_product = len(sales)
    total_revenue = sum(product['price'] * product['quantity'] for product in sales)
    high_revenue_product = max(sales, key = lambda x : x['price'] * x['quantity'])
    sorted_product = sorted(sales, key = lambda x : x['price'] * x['quantity'], reverse=True)
    revenue_5000_plus = [product['name'] for product in sales if product['price'] * product['quantity'] >= 5000]
    quantity_5_plus = list(filter(lambda x : x['quantity'] >= 5, sales))
    
    return {
        "Total products" : total_product,
        "Total revenue" : total_revenue,
        "Highest revenue" : high_revenue_product,
        "Revenue 5000+" : revenue_5000_plus,
        "Quantity 5+" : quantity_5_plus,
        "Sorted products": sorted_product
    }
    
print(analyze_sales(sales))
print(analyze_sales([]))