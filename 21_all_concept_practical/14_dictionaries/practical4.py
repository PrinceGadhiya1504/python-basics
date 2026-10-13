# Function analyze_employees(employees) banao jo:
# 1. Empty dictionary ho to "No employees available" return kare.
# 2. len() se total employees nikale.
# 3. items() aur loop se har employee ki details process kare.
# 4. sum() se total salary aur average salary nikale.
# 5. max() aur min() se highest aur lowest salary wale employee IDs nikale.
# 6. Dictionary comprehension se sirf IT department ke employees ka dictionary banaye.
# 7. Dictionary comprehension se ₹45,000 ya usse zyada salary wale employees nikale.
# 8. set() se unique departments nikale.
# 9. copy() se dictionary ki copy banaye aur employee ID 106 ke liye naya employee add kare: {"name": "Mihir", "department": "IT", "salary": 40000}.
# 10. Saare results dictionary mein return kare aur normal dictionary ke saath empty dictionary bhi test kare.
# Expected checks:
# - Total employees: 5
# - Total salary: 237000
# - Average salary: 47400
# - Highest salary employee ID: 104
# - Lowest salary employee ID: 102
# - Unique departments: {"IT", "HR", "Finance"}

employees = {
    101: {"name": "Amit", "department": "IT", "salary": 45000},
    102: {"name": "Neha", "department": "HR", "salary": 38000},
    103: {"name": "Raj", "department": "IT", "salary": 52000},
    104: {"name": "Priya", "department": "Finance", "salary": 60000},
    105: {"name": "Jay", "department": "HR", "salary": 42000}
}

def analyze_employees(employees):
    if not employees:
        return "No employees available"
  
    total_employee = len(employees)
    details = {}
    for emp_id, info in employees.items():
        details[emp_id] = info
    total_salary = sum(employees[ID]["salary"] for ID in employees)
    average_salary = total_salary / total_employee
    highest_salary = max(employees, key = lambda ID : employees[ID]["salary"])
    lowest_salary = min(employees, key = lambda ID : employees[ID]["salary"])
    it_department = {key : value for key, value in employees.items() if value["department"] == "IT"}
    above_45k = {key : value for key, value in employees.items() if value["salary"] >= 45000}
    unique_departments = set(employees[ID]["department"] for ID in employees)
    copy_employee = employees.copy()
    copy_employee[106] = {"name": "Mihir", "department": "IT", "salary": 40000}
    
    return {
        "total_employee": total_employee,
        "details": details,
        "total_salary": total_salary,
        "average_salary": average_salary,
        "highest_salary": highest_salary,
        "lowest_salary": lowest_salary,
        "it_department": it_department,
        "above_45k": above_45k,
        "unique_departments": unique_departments,
        "copy_employee": copy_employee
    }
    
print(analyze_employees(employees))