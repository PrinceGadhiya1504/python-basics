# Function analyze_orders(orders) banao:
# 1. Empty tuple ho toh "No orders available" return karo.
# 2. len() se total orders count karo.
# 3. sum() se completed orders ka total amount nikalo.
# 4. filter() se poore pending order tuples nikalo.
# 5. max() se highest amount wala poora order tuple nikalo.
# 6. sorted() aur lambda se amount ke descending order mein sort karo.
# 7. count() se check karo ki exact tuple (102, "Neha", 5000, "pending") kitni baar hai.
# 8. Set comprehension se unique customer names nikalo.
# 9. List comprehension se ₹3,000 ya usse zyada amount wale poore order tuples nikalo.
# 10. Results dictionary mein return karo aur empty tuple bhi test karo.
# Expected output
# {
#     "total_orders": 6,
#     "completed_total": 14700,
#     "pending_orders": [
#         (102, "Neha", 5000, "pending")
#     ],
#     "highest_order": (104, "Priya", 7000, "completed"),
#     "pending_tuple_count": 1,
#     "unique_customers": {"Amit", "Neha", "Raj", "Priya", "Jay"},
#     "orders_3000_plus": [
#         (102, "Neha", 5000, "pending"),
#         (104, "Priya", 7000, "completed"),
#         (105, "Jay", 3000, "cancelled"),
#         (106, "Neha", 4000, "completed")
#     ]
# }
# No orders available

orders = (
    (101, "Amit", 2500, "completed"),
    (102, "Neha", 5000, "pending"),
    (103, "Raj", 1200, "completed"),
    (104, "Priya", 7000, "completed"),
    (105, "Jay", 3000, "cancelled"),
    (106, "Neha", 4000, "completed")
)

def analyze_orders(orders):
    if not orders:
        return "No orders available"

    total_orders = len(orders)
    completed_total = sum(order[2] for order in orders if order[3] == "completed")
    pending_orders = list(filter(lambda order: order[3] == "pending", orders))
    highest_order = max(orders, key=lambda x: x[2])
    sorted_orders = sorted(orders, key=lambda x: x[2], reverse=True)
    pending_tuple_count = orders.count((102, "Neha", 5000, "pending"))
    unique_customers = set(order[1] for order in orders)
    orders_3000_plus = list(filter(lambda order: order[2] >= 3000, orders))
    
    return {
        "total_orders": total_orders,
        "completed_total": completed_total,
        "pending_orders": pending_orders,
        "highest_order": highest_order,
        "sorted_orders": sorted_orders,
        "pending_tuple_count": pending_tuple_count,
        "unique_customers": unique_customers,
        "orders_3000_plus": orders_3000_plus
    }

print(analyze_orders(orders))
print(analyze_orders(()))