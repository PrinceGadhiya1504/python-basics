employees = [
    {"name": "Amit", "salary": 45000},
    {"name": "Neha", "salary": 65000},
    {"name": "Raj", "salary": 30000},
    {"name": "Priya", "salary": 80000},
    {"name": "Karan", "salary": 55000}
]

# calculate_bonus() function banaye:
    # - Salary 60,000 ya usse zyada ho to 10% bonus.
    # - Salary 40,000 se 59,999 ho to 7% bonus.
    # - Salary 40,000 se kam ho to 5% bonus.
# Har employee ka bonus calculate karke dictionary me bonus key add kare.
# try-except se invalid salary type ya negative salary handle kare.
# Loop se employee ka naam, salary aur bonus print kare.
# filter() se 60,000 ya usse zyada salary wale employees nikale.
# sorted() se employees ko total compensation (salary + bonus) ke descending order me sort kare.

def calculate_bonus(employees):
    if type(employees['salary']) not in (int, float):
        raise TypeError("Salary must be a number")

    elif employees['salary'] < 0:
        raise ValueError("Salary cannot be negative")

    elif employees['salary'] >= 60000:
        return employees['salary'] * 0.10

    elif employees['salary'] >= 40000:
        return employees['salary'] * 0.07

    else:
        return employees['salary'] * 0.05

for emp in employees:
    try:
        emp['bonus'] = calculate_bonus(emp)
    except ValueError:
        emp['bonus'] = "Invalid"
    except TypeError:
        emp['bonus'] = "Invalid"

print("Employee Report:")
for emp in employees:
    print(f"Name: {emp['name']}, Salary: {emp['salary']}, Bonus: {emp['bonus']}")

print("\n Employee with salary more than 60000")
emp = list(filter(
    lambda x: type(x['salary']) in (int, float) and x['salary'] >= 60000,
    employees
))
for e in emp:
    print(f"Name: {e['name']}, Salary: {e['salary']}, Bonus: {e['bonus']}")

print("Employee total compensation")
sorted_emp = sorted(employees, key=lambda x: x['salary'] + x['bonus'] if x['bonus'] != 'Invalid' else 0, reverse=True)
for i in sorted_emp:
    print(f"Name: {i['name']}, Salary: {i['salary']}, Bonus: {i['bonus']}, Total: {i['salary'] + i['bonus'] if i['bonus'] != 'Invalid' else 'Invalid'}")