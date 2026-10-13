# Function analyze_employees(employees) banao:
# 1. Empty tuple ho toh "No employee data" return karo.
# 2. len() se total employees count karo.
# 3. Tuple unpacking se name, salary, bonus aur department nikalo.
# 4. Har employee ka total compensation (salary + bonus) calculate karo.
# 5. sum() se total compensation aur average compensation nikalo.
# 6. max() aur min() se highest aur lowest compensation wale poore employee tuples nikalo.
# 7. sorted() aur lambda se compensation ke descending order mein sort karo.
# 8. any() se check karo ki kisi employee ka compensation ₹50,000 se zyada hai.
# 9. all() se check karo ki sabhi employees ki salary ₹20,000 ya usse zyada hai.
# 10. Unique departments ka set banao aur saare results dictionary mein return karo.
# Expected output
# {
#     "total_employees": 5,
#     "total_compensation": 245000,
#     "average_compensation": 49000.0,
#     "highest_employee": ("Priya", (50000, 10000), "Finance"),
#     "lowest_employee": ("Raj", (18000, 2000), "IT"),
#     "any_compensation_above_50000": True,
#     "all_salary_20000_plus": False,
#     "unique_departments": {"IT", "HR", "Finance"}
# }
# No employee data

employees = (
    ("Amit", (25000, 5000), "IT"),
    ("Neha", (40000, 8000), "HR"),
    ("Raj", (18000, 2000), "IT"),
    ("Priya", (50000, 10000), "Finance"),
    ("Jay", (32000, 4000), "HR")
)

def analyze_employees(employees):
    if not employees:
        return "No employee data"
    
    total_employees = len(employees)
    
    total_compensation = 0
    for name, (salary, bonus), department in employees:
        total_compensation += salary + bonus

    # total_compensation = sum(employee[1][0] + employee[1][1] for employee in employees)
    average_compensation = total_compensation / total_employees
    highest_employee = max(employees, key=lambda x: x[1][0] + x[1][1])
    lowest_employee = min(employees, key=lambda x: x[1][0] + x[1][1])
    any_compensation_above_50000 = any(employee[1][0] + employee[1][1] > 50000 for employee in employees)
    all_salary_20000_plus = all(employee[1][0] >= 20000 for employee in employees)
    unique_departments = set(employee[2] for employee in employees)
    
    return {
        "total_employees": total_employees,
        "total_compensation": total_compensation,
        "average_compensation": average_compensation,
        "highest_employee": highest_employee,
        "lowest_employee": lowest_employee,
        "any_compensation_above_50000": any_compensation_above_50000,
        "all_salary_20000_plus": all_salary_20000_plus,
        "unique_departments": unique_departments
    }

print(analyze_employees(employees))
print(analyze_employees(()))