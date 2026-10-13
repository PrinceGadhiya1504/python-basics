# Function withdraw_money(accounts, name, amount) banao jo:
# 1. Agar name account mein nahi hai, to KeyError raise kare.
# 2. Agar amount integer nahi hai, to TypeError raise kare. bool ko valid amount mat maanna.
# 3. Agar amount zero ya negative hai, to ValueError raise kare.
# 4. Agar balance se zyada amount withdraw ho raha hai, to custom message "Insufficient balance" return kare.
# 5. Valid withdrawal par balance update kare aur remaining balance return kare.
# 6. except blocks se errors handle kare.
# 7. else mein successful withdrawal ka message print kare.
# 8. finally mein "Transaction completed" print kare.
# 9. In cases ko test kare:

# Expected results:
# - Amit → remaining balance 4000
# - Neha → "Insufficient balance"
# - Jay → "Account not found"
# - Raj with -100 → "Amount must be positive"
# - Raj with "200" → "Amount must be an integer"

accounts = {
    "Amit": 5000,
    "Neha": 3000,
    "Raj": 1000
}

def withdraw_money(accounts, name, amount):
    try:
        if name not in accounts:
            raise KeyError

        if type(amount) is not int:
            raise TypeError

        if amount <= 0:
            raise ValueError

        if amount > accounts[name]:
            return "Insufficient balance"

        accounts[name] -= amount

    except KeyError:
        return "Account not found"

    except TypeError:
        return "Amount must be an integer"

    except ValueError:
        return "Amount must be positive"

    else:
        print("Withdrawal successful")
        return accounts[name]

    finally:
        print("Transaction completed")


print(withdraw_money(accounts, "Amit", 1000))
print(withdraw_money(accounts, "Neha", 5000))
print(withdraw_money(accounts, "Jay", 500))
print(withdraw_money(accounts, "Raj", -100))
print(withdraw_money(accounts, "Raj", "200"))