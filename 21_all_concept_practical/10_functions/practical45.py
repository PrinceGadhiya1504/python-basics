# Task:
# 1. show_order(customer="Guest", *items, **details) naam ka function banao.
# 2. Function ke andar customer ka naam print karo.
# 3. items mein aaye saare items ko for loop se print karo.
# 4. details dictionary ki har key aur value ko .items() se print karo.
# 5. Function ko is tarah call karo:
    # show_order(
    #     "Prince",
    #     "Laptop",
    #     "Mouse",
    #     city="Ahmedabad",
    #     payment="UPI"
    # )

# Expected output:
# Customer: Prince
# Item: Laptop
# Item: Mouse
# city: Ahmedabad
# payment: UPI

def show_order(customer="Guest", *items, **details):
    print("Customer:", customer)
    for item in items:
        print(f"Item: {item}")
    for key, value in details.items():
        print(f"{key}: {value}")

show_order(
    "Prince",
    "Laptop",
    "Mouse",
    city="Ahmedabad",
    payment="UPI"
)