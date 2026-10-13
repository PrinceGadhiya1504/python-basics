# Function analyze_inventory(warehouse_a, warehouse_b) banao jo:
# 1. Dono warehouses ke saare unique products nikale.
# 2. Dono warehouses mein common products nikale.
# 3. Sirf warehouse A ke products nikale.
# 4. Sirf warehouse B ke products nikale.
# 5. symmetric_difference() se alag-alag products nikale.
# 6. Set comprehension se "M" letter se start hone wale products nikale.
# 7. Dono sets ko list mein convert karke unhe alphabetically sort kare.
# 8. frozenset() se unique products ka immutable set banaye.
# 9. any() check kare ki koi product "P" se start hota hai ya nahi.
# 10. Dictionary mein saare results return kare.
# Expected output checks:
# - Unique products ki count: 6
# - Common products: {"Mouse", "Monitor"}
# - Warehouse A only: {"Laptop", "Keyboard"}
# - Warehouse B only: {"Printer", "Scanner"}
# - "M" se start hone wale products: {"Mouse", "Monitor"}
# - any() ka result: True

warehouse_a = {"Laptop", "Mouse", "Keyboard", "Monitor"}
warehouse_b = {"Mouse", "Printer", "Monitor", "Scanner"}

def analyze_inventory(warehouse_a, warehouse_b):
    unique_products = warehouse_a.union(warehouse_b)
    common_products = warehouse_a.intersection(warehouse_b)
    warehouse_a_only = warehouse_a.difference(warehouse_b)
    warehouse_b_only = warehouse_b.difference(warehouse_a)
    symmetric_difference = warehouse_a.symmetric_difference(warehouse_b)
    m_products = {product for product in unique_products if product.startswith("M")}
    sorted_list = sorted(list(unique_products))
    frozenset_products = frozenset(unique_products)
    any_p_products = any(product.startswith("P") for product in unique_products)
    
    return {
        "unique_products": unique_products,
        "common_products": common_products,
        "warehouse_a_only": warehouse_a_only,
        "warehouse_b_only": warehouse_b_only,
        "symmetric_difference": symmetric_difference,
        "m_products": m_products,
        "sorted_list": sorted_list,
        "frozenset_products": frozenset_products,
        "any_p_products": any_p_products
    }

print(analyze_inventory(warehouse_a, warehouse_b))