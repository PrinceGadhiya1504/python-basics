# Task: Employee Salary Analyzer
# analyze_salaries(employees) function banao:
# 1. Empty list ho to "No employees available" return karo.
# 2. sum() aur len() se average salary calculate karo.
# 3. max() aur min() se highest aur lowest salary wale employees find karo.
# 4. sorted() aur lambda se salary ke descending order mein employees sort karo.
# 5. List comprehension se ₹30,000 ya usse zyada salary wale employees select karo.
# 6. Sabhi results ek dictionary mein return karo.
# 7. Function ko normal list aur empty list ke saath test karo.
# Expected output:
# {
#     'average_salary': 33000.0,
#     'highest_paid': ['Priya', 50000],
#     'lowest_paid': ['Raj', 18000],
#     'sorted_employees': [
#         ['Priya', 50000],
#         ['Neha', 40000],
#         ['Jay', 32000],
#         ['Amit', 25000],
#         ['Raj', 18000]
#     ],
#     'salary_30000_or_more': [
#         ['Neha', 40000],
#         ['Priya', 50000],
#         ['Jay', 32000]
#     ]
# }
# No employees available

employees = [
    ["Amit", 25000],
    ["Neha", 40000],
    ["Raj", 18000],
    ["Priya", 50000],
    ["Jay", 32000]
]

def analyze_salaries(employees):
    if not employees:
        return "No employees available"
    
    average_salary = sum(employee[1] for employee in employees) / len(employees)
    highest_paid = max(employees, key = lambda x : x[1])
    lowest_paid = min(employees, key = lambda x : x[1])
    sorted_salary = sorted(employees, key = lambda x : x[1], reverse=True)
    salary_30000_or_more = list(filter(lambda x : x[1] >= 30000, employees))

    return{
        "average_salary": average_salary,
        "highest_paid": highest_paid,
        "lowest_paid": lowest_paid,
        "sorted_employees": sorted_salary,
        "salary_30000_or_more": salary_30000_or_more
    }

print(analyze_salaries(employees))
print(analyze_salaries([]))