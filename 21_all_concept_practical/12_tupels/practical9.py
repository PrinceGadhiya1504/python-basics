# Function update_inventory(inventory, product_name, new_stock) banao:
# 1. Empty inventory ho toh "Inventory is empty" return karo.
# 2. any() se check karo ki product inventory mein exist karta hai ya nahi.
# 3. Agar product nahi milta, toh "Product not found" return karo.
# 4. Tuple ko list mein convert karo.
# 5. Loop aur tuple unpacking se matching product ka stock update karo.
# 6. Updated list ko wapas tuple mein convert karo.
# 7. sum() se updated total stock nikalo.
# 8. sorted() aur lambda se stock descending order mein sort karo.
# 9. Updated inventory, total stock aur sorted inventory dictionary mein return karo.
# 10. Ye 3 cases test karo: existing product, missing product, aur empty inventory.
# Expected output — existing product
# Function call:
# print(update_inventory(inventory, "Mouse", 40))

# {
#     "updated_inventory": (
#         ("Laptop", 10),
#         ("Mouse", 40),
#         ("Keyboard", 15),
#         ("Monitor", 8)
#     ),
#     "total_stock": 73,
#     "sorted_inventory": [
#         ("Mouse", 40),
#         ("Keyboard", 15),
#         ("Laptop", 10),
#         ("Monitor", 8)
#     ]
# }

inventory = (
    ("Laptop", 10),
    ("Mouse", 25),
    ("Keyboard", 15),
    ("Monitor", 8)
)

def update_inventory(inventory, product_name, new_stock):
    if not inventory:
        return "Inventory is empty"

    product_exist = any(i[0] == product_name for i in inventory)
    if not product_exist:
        return "Product not found"

    inv_list = list(inventory)
    for i in range(len(inv_list)):
        if inv_list[i][0] == product_name:
            inv_list[i] = (product_name, new_stock)
            break
    inv_tuple = tuple(inv_list)
    total_stock = sum(i[1] for i in inv_tuple)
    sorted_inventory = sorted(inv_tuple, key=lambda x: x[1], reverse=True)

    return {
        "updated_inventory": inv_tuple,
        "total_stock": total_stock,
        "sorted_inventory": sorted_inventory
    }

print(update_inventory(inventory, "Tablet", 20))
print(update_inventory((), "Mouse", 40))