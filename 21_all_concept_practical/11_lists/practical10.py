# Ek function analyze_orders(orders) banao.
# 1. Validation: Empty list ho toh "No orders available" return karo.
# 2. len() — total orders count karo.
# 3. sum() — completed orders ka total amount nikalo.
# 4. filter() — pending orders nikalo.
# 5. List comprehension — completed orders ki list banao.
# 6. max() — sabse zyada amount wala order nikalo.
# 7. sorted() + lambda — orders ko amount ke descending order mein sort karo.
# 8. Set — unique customer names nikalo.
# 9. Saare results ek dictionary mein return karo.
# 10. Normal aur empty list dono test karo.

# Expected results
# Result		            Expected value
# Total orders		             6
# Completed orders ka total	           ₹14,700
# Pending customer		             Neha
# Highest amount order	             Priya — ₹7,000
# Unique customers		             Amit, Neha, Raj, Priya, Jay

orders = [
    {"customer": "Amit", "amount": 2500, "status": "completed"},
    {"customer": "Neha", "amount": 5000, "status": "pending"},
    {"customer": "Raj", "amount": 1200, "status": "completed"},
    {"customer": "Priya", "amount": 7000, "status": "completed"},
    {"customer": "Jay", "amount": 3000, "status": "cancelled"},
    {"customer": "Neha", "amount": 4000, "status": "completed"}
]

def analyze_orders(orders):
    if not orders:
        return "No orders available"

    total_order = len(orders)
    completed_order_total = sum(order['amount'] for order in orders if order['status'] == 'completed')
    pending_order = list(filter(lambda x : x['status'] == 'pending', orders))
    completed_order = [order['customer'] for order in orders if order['status'] == 'completed']
    high_amount_order = max(orders, key= lambda x:x['amount'])
    sorted_order = sorted(orders, key= lambda x:x['amount'], reverse=True)
    unique_customer = set(order['customer'] for order in orders)
    return {
        "Total orders": total_order,
        "Completed orders ka total": completed_order_total,
        "Pending customer": pending_order,
        "Highest amount order": high_amount_order,
        "Sorted orders": sorted_order,
        "Unique customers": unique_customer
    }

print(analyze_orders(orders))
print(analyze_orders([]))