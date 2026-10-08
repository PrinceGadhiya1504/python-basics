# Employee Management - File Handling + Loop

total_employees = int(input("How many employees do you want to add? "))
with open("employees.txt", "a", encoding="utf-8") as file:
    for i in range(total_employees):
        print(f"\nEnter details for Employee {i + 1}")

        name = input("Enter employee name: ")
        age = input("Enter employee age: ")
        department = input("Enter employee department: ")
        salary = input("Enter employee salary: ")

        # Add employee details to file
        file.write("Employee Details\n")
        file.write("Name: " + name + "\n")
        file.write("Age: " + age + "\n")
        file.write("Department: " + department + "\n")
        file.write("Salary: " + salary + "\n")
        file.write("------------------------\n")

print("\nAll employee details saved successfully!")

# Read all employee details
print("\n========== ALL EMPLOYEES ==========\n")

with open("employees.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)