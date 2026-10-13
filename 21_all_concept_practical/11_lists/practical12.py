# Function analyze_transactions(transactions) banao:
# 1. Empty list ho toh "No transactions available" return karo.
# 2. Total transactions count karo.
# 3. sum() se total income aur total expenses calculate karo.
# 4. Income minus expenses se final balance nikalo.
# 5. filter() se poore income transactions nikalo.
# 6. List comprehension se ₹1,000 se zyada amount wale poore transactions nikalo.
# 7. max() se highest-amount transaction nikalo.
# 8. sorted() aur lambda se amount ke descending order mein transactions sort karo.
# 9. Set comprehension se unique categories nikalo.
# 10. Saare results dictionary mein return karo; normal aur empty list dono test karo.

# Expected output
# {
#     "total_transactions": 6,
#     "total_income": 30000,
#     "total_expenses": 5100,
#     "balance": 24900,
#     "income_transactions": [
#         {"id": 103, "category": "Salary", "amount": 25000, "type": "income"},
#         {"id": 105, "category": "Freelance", "amount": 5000, "type": "income"}
#     ],
#     "transactions_above_1000": [
#         {"id": 102, "category": "Travel", "amount": 1500, "type": "expense"},
#         {"id": 103, "category": "Salary", "amount": 25000, "type": "income"},
#         {"id": 104, "category": "Shopping", "amount": 2200, "type": "expense"},
#         {"id": 105, "category": "Freelance", "amount": 5000, "type": "income"}
#     ],
#     "highest_transaction": {
#         "id": 103, "category": "Salary", "amount": 25000, "type": "income"
#     },
#     "sorted_transactions": "... all 6 transactions, descending by amount ...",
#     "unique_categories": {"Food", "Travel", "Salary", "Shopping", "Freelance"}
# }
# No transactions available

transactions = [
    {"id": 101, "category": "Food", "amount": 800, "type": "expense"},
    {"id": 102, "category": "Travel", "amount": 1500, "type": "expense"},
    {"id": 103, "category": "Salary", "amount": 25000, "type": "income"},
    {"id": 104, "category": "Shopping", "amount": 2200, "type": "expense"},
    {"id": 105, "category": "Freelance", "amount": 5000, "type": "income"},
    {"id": 106, "category": "Food", "amount": 600, "type": "expense"}
]

def sorted_transactions(transactions):
    if not transactions:
        return "No transactions available"

    total_transactions = len(transactions)
    total_income = sum(transaction['amount'] for transaction in transactions if transaction['type'] == 'income')
    total_expenses = sum(transaction['amount'] for transaction in transactions if transaction['type'] == 'expense')
    final_balance = total_income - total_expenses
    income_transactions = list(filter(lambda x : x['type'] == 'income', transactions))
    transactions_above_1000 = [t for t in transactions if t['amount'] > 1000]
    highest_transaction = max(transactions, key=lambda x: x['amount'])
    sorted_transactions = sorted(transactions, key=lambda x: x['amount'], reverse=True)
    unique_categories = {transaction['category'] for transaction in transactions}

    return {
        "total_transactions": total_transactions,
        "total_income": total_income,
        "total_expenses": total_expenses,
        "balance": final_balance,
        "income_transactions": income_transactions,
        "transactions_above_1000": transactions_above_1000,
        "highest_transaction": highest_transaction,
        "sorted_transactions": sorted_transactions,
        "unique_categories": unique_categories
    }

print(sorted_transactions(transactions))
print(sorted_transactions([]))