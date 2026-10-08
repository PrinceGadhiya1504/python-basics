import employeesmodule as empms

# Print all employees
print('All employees:')
for x in empms.employees:
    print(x)
    
# Print Name and City
print('\n\n Name and city:')
for x in empms.employees:
    print('--------------')
    print('name: ', x.get("name"))
    print('city: ', x.get("city"))


# Age 25 and above
print('\n\n Age 25 and above:')
for x in empms.employees:
    if x.get("age") >= 25:
        print('--------------')
        print('name: ', x.get("name"))
        print('age: ', x.get("age"))

# Age wise sorting DESC
print("\n\n Age wise sorting DESC:")
for x in sorted(empms.employees, key=lambda x: x.get("age"), reverse=True):
    print('--------------')
    print('name: ', x.get("name"))
    print('age: ', x.get("age"))