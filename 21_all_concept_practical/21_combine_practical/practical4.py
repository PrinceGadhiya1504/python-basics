# Ek program banao jo:
# 1. get_expense_status() function banaye:
#    - Amount 1000 se zyada ho → "High"
#    - Amount 500 se zyada ho aur 1000 tak ho → "Medium"
#    - Amount 500 ya usse kam ho → "Low"
# 2. Har expense ke dictionary me status key add kare.
# 3. Negative ya non-numeric amount ko try-except se handle kare.
# 4. Loop se saare expenses aur unka status print kare.
# 5. filter() se sirf "High" expenses select kare.
# 6. sorted() se expenses ko amount ke descending order me sort kare.
# 7. map() se har expense ka message banao, jaise "Food: 250".
# 8. Function ki help se total valid expenses calculate karo.
# Expected output
# Expense Report:
# Food: 250 - Low
# Travel: 500 - Low
# Shopping: 1200 - High
# Food: 350 - Low
# Travel: 150 - Low
# Bills: 800 - Medium

# High Expenses:
# Shopping: 1200

# Sorted Expenses:
# Shopping: 1200
# Bills: 800
# Travel: 500
# Food: 350
# Food: 250
# Travel: 150

# Expense Messages:
# ['Food: 250', 'Travel: 500', 'Shopping: 1200',
#  'Food: 350', 'Travel: 150', 'Bills: 800']

# Total Expenses: 3250

expenses = [
    {"category": "Food", "amount": 250},
    {"category": "Travel", "amount": 500},
    {"category": "Shopping", "amount": 1200},
    {"category": "Food", "amount": 350},
    {"category": "Travel", "amount": 150},
    {"category": "Bills", "amount": 800}
]

def get_expense_status(expenses):
    amount = expenses['amount']

    if type(amount) not in (int, float):
        raise TypeError("Amount must be a number")

    if amount < 0:
        raise ValueError("Amount cannot be negative")

    if amount > 1000:
        return "High"

    if amount > 500:
        return "Medium"

    return "Low"

for ex in expenses:
    try:
        ex['status'] = get_expense_status(ex)
    except (TypeError, ValueError):
        ex['status'] = "Invalid"

print("Expense Report:")
for ex in expenses:
    print(f"{ex['category']}: {ex['amount']} - {ex['status']}")

print("\nHigh Expenses:")
high_expenses = list(filter(lambda ex: ex['status'] == "High", expenses))
for ex in high_expenses:
    print(f"{ex['category']}: {ex['amount']}")

print("\nSorted Expenses:")
sorted_expenses = sorted(expenses, key=lambda ex: ex['amount'],reverse=True)
for ex in sorted_expenses:
    print(f"{ex['category']}: {ex['amount']}")

print("\nExpense Messages:")
expense_messages = list(map(lambda ex: f"{ex['category']}: {ex['amount']}", expenses))
print(expense_messages)

print("\nTotal Expenses:")
total_expenses = sum(ex['amount'] for ex in expenses if ex['status'] != "Invalid")
print(total_expenses)