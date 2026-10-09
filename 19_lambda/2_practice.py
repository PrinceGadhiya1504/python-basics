# Practice 1
# Create a lambda function that takes a number and returns its square.
from xdg import Exceptions
square = lambda x : x * x
print(square(5))

# Practice 2 — Multiple Arguments
# Create a lambda function that takes two numbers and returns their sum.
twonum = lambda x, y : x + y
print(twonum(10, 20))

# Practice 3 — Default Argument
# Create a lambda function that:
#     Takes two numbers: x and y
#     y should have a default value of 10
#     Returns x + y
add = lambda x, y = 10 : x + y
print(add(5))
print(add(5, 20))

# Practice 4 — *args
# Create a lambda function that can accept any number of numbers and returns their total.
total = lambda *args: sum(args)
print(total(10, 20, 30))
print(total(5, 10, 15, 20))

# Practice 5 — **kwargs
# Create a lambda function that accepts any number of keyword arguments using **kwargs and returns the kwargs dictionary.
show_data = lambda **kwargs: kwargs
print(show_data(name="Prince", age=23, city="Ahmedabad"))

# Practice 6 — Conditional Lambda
# Create a lambda function that takes a number and returns:
#   "Even" if the number is even
#   "Odd" if the number is odd
check_number = lambda x : "Even" if x % 2 == 0 else "Odd"
print(check_number(10))
print(check_number(7))

# Practice 7 — map() + Lambda
# Now let's start the important part: lambda with built-in functions.
numbers = [1, 2, 3, 4, 5]
double = list(map(lambda x : x * 2, numbers))
print(double)

# Practice 8 — map() + Lambda
# Use map() + lambda to calculate the square of every number.
square_num = list(map(lambda x : x * x, numbers))
print(square_num)

# Practice 9 — map() + Lambda with Strings
# Use map() + lambda to convert every name to uppercase.
names = ["prince", "rahul", "amit", "rohit"]
uppercase_name = list(map(lambda x : x.upper(), names))
print(uppercase_name)

# Practice 10 — filter() + Lambda
# Use filter() + lambda to get only even numbers.
numbers = [10, 15, 20, 25, 30, 35, 40]
even_number = list(filter(lambda x : x % 2 == 0, numbers))
print(even_number)

# Practice 11 — filter() + Lambda
# Use filter() + lambda to get only numbers greater than 20.
numbers = [5, 12, 18, 7, 25, 30, 9, 40]
grater_number = list(filter(lambda x : x >= 20, numbers))
print(grater_number)

# Practice 12 — filter() + Lambda with Strings
# Use filter() + lambda to select only names whose length is greater than 5.
names = ["Prince", "Raj", "Rahul", "Amit", "Alexander"]
long_name = list(filter(lambda x : len(x) > 5, names))
print(long_name)

# Practice 13 — reduce() + Lambda
# Use reduce() + lambda to calculate the sum of all numbers.
numbers = [1, 2, 3, 4, 5]
from functools import reduce
sum_num = reduce(lambda x, y : x + y, numbers)
print(sum_num)

# Practice 14 — reduce() + Lambda
# Use reduce() + lambda to multiply all numbers together.
sum_num = reduce(lambda x, y : x * y, numbers)
print(sum_num)

# Practice 15 — sorted() + Lambda
# Use sorted() + lambda to sort the users by age from lowest to highest.
users = [
    {"name": "Prince", "age": 23},
    {"name": "Rahul", "age": 30},
    {"name": "Amit", "age": 20},
    {"name": "Rohit", "age": 27}
]
sorted_users = sorted(users, key = lambda x : x["age"])
print(sorted_users)

# Practice 16 — sorted() + Lambda + reverse
# Using the same users list, sort the users by age from highest to lowest.
sorted_users = sorted(users, key = lambda x : x["age"], reverse=True)
print(sorted_users)

# Practice 17 — min() + Lambda
# Use min() + lambda to find the user with the lowest age.
min_age_user = min(users, key = lambda x : x['age'])
print(min_age_user)

# Practice 18 — max() + Lambda
# Using the same users list, find the user with the highest age.
max_age_user = max(users, key = lambda x : x["age"])
print(max_age_user)

# Practice 19 — Lambda with Dictionaries
# Use filter() + lambda to select products whose price is greater than ₹5,000.
products = [
    {"name": "Laptop", "price": 70000},
    {"name": "Mouse", "price": 1000},
    {"name": "Keyboard", "price": 2000},
    {"name": "Monitor", "price": 15000}
]
grater_price = list(filter(lambda x : x["price"] >= 5000, products))
print(grater_price)

# Practice 20 — filter() + Lambda
# filter() + lambda use karke sirf un products ko select karo jinka price ₹5,000 se kam hai.
less_price = list(filter(lambda x : x["price"] < 5000, products))
print(less_price)

# Practice 21 — map() + filter() together
# Task:
    # filter() + lambda se sirf even numbers select karo.
    # map() + lambda se selected numbers ko double karo.
numbers = [5, 10, 15, 20, 25, 30, 35, 40]
even_num = list(filter(lambda x : x % 2 == 0, numbers))
double_num = list(map(lambda x : x * 2, even_num))
print(double_num)

# Practice 22 — sorted() with strings
# Use sorted() + lambda to sort the names by length, from shortest to longest.
names = ["Prince", "Raj", "Rahul", "Amit", "Alexander"]
sort_name = sorted(names, key = lambda x : len(x))
print(sort_name)

# Practice 23 — sorted() by Dictionary Value
# Use sorted() + lambda to sort employees by salary from highest to lowest.
employees = [
    {"name": "Prince", "salary": 30000},
    {"name": "Rahul", "salary": 45000},
    {"name": "Amit", "salary": 25000},
    {"name": "Rohit", "salary": 40000}
]
sort_salary = sorted(employees, key = lambda x : x['salary'], reverse=True)
print(sort_salary)

# Practice 24 — filter() + Lambda with Nested Data
# Use filter() + lambda to select only employees who work in the "Development" department.
employees = [
    {"name": "Prince", "department": "Development", "salary": 50000},
    {"name": "Rahul", "department": "Testing", "salary": 40000},
    {"name": "Amit", "department": "Development", "salary": 60000},
    {"name": "Rohit", "department": "HR", "salary": 35000}
]
filter_department = list(filter(lambda x : x['department'] == 'Development', employees))
print(filter_department)

# Practice 25 — map() + Lambda with Dictionaries
# Use map() + lambda to extract only the employee names into a list.
emp_names = list(map(lambda x : x['name'], employees))
print(emp_names)

# Practice 26 — map() + Lambda with Calculations
# Use map() + lambda to create a list containing each product's price after adding 18% tax.
products = [
    {"name": "Laptop", "price": 1000},
    {"name": "Mouse", "price": 200},
    {"name": "Keyboard", "price": 500}
]
product_price = list(map(lambda x : x['price'] + (x['price'] * 0.18), products))
print(product_price)

# Practice 27 — Lambda Returning Lambda
# Create a normal function called multiplier that accepts n and returns a lambda that multiplies x by n.
def multiplier(n):
    return lambda x : x * n
double = multiplier(2)
triple = multiplier(3)
print(double(5))
print(triple(5))  

# Practice 28 — Final Challenge: Lambda with Real-World Data
# task:
#     1. Use filter() + lambda to select employees from the "Development" department.
#     2. Use map() + lambda to extract their names.
#     3. Print the final list of names.
employees = [
    {"name": "Prince", "department": "Development", "salary": 50000},
    {"name": "Rahul", "department": "Testing", "salary": 40000},
    {"name": "Amit", "department": "Development", "salary": 60000},
    {"name": "Rohit", "department": "HR", "salary": 35000},
    {"name": "Jay", "department": "Development", "salary": 45000}
]
# department_filter = list(filter(lambda x : x['department'] == 'Development', employees))
# emp_name = list(map(lambda x : x['name'], department_filter))
emp_names = list(map(lambda x : x['name'], filter(lambda x : x['department'] == 'Development', employees)))
print(emp_names)

# Practice 29 — Lambda with min() and max()
# Task: min() aur max() ke saath lambda use karke:
#     1. Sabse sasta product find karo.
#     2. Sabse expensive product find karo.
products = [
    {"name": "Laptop", "price": 70000},
    {"name": "Mouse", "price": 1000},
    {"name": "Keyboard", "price": 2000},
    {"name": "Monitor", "price": 15000}
]
low_price_product = min(products, key=lambda x : x['price'])
high_price_product = max(products, key=lambda x : x['price'])
print(low_price_product)
print(high_price_product)

# Practice 30 — Lambda with sorted(), filter() and map()
# Task:
    # 1. filter() + lambda se ₹5,000 se zyada price wale products select karo.
    # 2. sorted() + lambda se unhe lowest se highest price tak sort karo.
    # 3. map() + lambda se sirf product names extract karo.
products = [
    {"name": "Laptop", "price": 70000},
    {"name": "Mouse", "price": 1000},
    {"name": "Keyboard", "price": 2000},
    {"name": "Monitor", "price": 15000},
    {"name": "Mobile", "price": 25000}
]
product_name = list(map(lambda x : x['name'], sorted(filter(lambda x : x['price'] > 5000, products), key= lambda x : x['price'])))
print(product_name)

# Practice 31 — lambda with any() and all()
# Task:
#     any() aur lambda ka use karke check karo ki list mein koi number > 45 hai ya nahi.
#     all() aur lambda ka use karke check karo ki list ke sabhi numbers > 5 hain ya nahi.
numbers = [10, 20, 30, 40, 50]
any_num = any(map(lambda x : x > 45, numbers))
all_num = all(map(lambda x : x > 5, numbers))
print(any_num)
print(all_num)

# Practice 32 — Thoda challenging
# Task:
#     any() se check karo ki koi number 40 se bada hai ya nahi.
#     all() se check karo ki sabhi numbers even hain ya nahi.
#     Dono questions mein lambda aur map() ka use karo.
numbers = [12, 18, 25, 30, 42]
any_num = any(map(lambda x : x > 40, numbers))
all_num = all(map(lambda x : x % 2 == 0, numbers))
print(any_num)
print(all_num)

# Next Practice 33 — lambda with sorted()
# sorted() aur lambda use karke:
#     1. Students ko marks ke basis par highest se lowest sort karo.
#     2. Sorted students ke sirf names print karo, marks nahi.
students = [
    {"name": "Rahul", "marks": 75},
    {"name": "Amit", "marks": 90},
    {"name": "Priya", "marks": 60},
    {"name": "Jay", "marks": 85}
]
student = list(map(lambda x : x['name'], sorted(students, key = lambda x : x['marks'], reverse=True)))
print(student)

# Practice 34 — lambda with filter() and all()
# Task:
#     1. filter() aur lambda se 80 ya usse zyada marks wale students select karo.
#     2. map() aur lambda se un students ke names nikalo.
#     3. all() aur lambda se check karo ki selected students ke sabhi marks 80 ya usse zyada hain.
students = [
    {"name": "Rahul", "marks": 75},
    {"name": "Amit", "marks": 90},
    {"name": "Priya", "marks": 60},
    {"name": "Jay", "marks": 85}
]
student_mark = list(filter(lambda x : x['marks'] >= 80, students))
student_name = list(map(lambda x : x['name'], student_mark))
all_student = all(map(lambda x : x['marks'] >= 80, student_mark))
print(student_mark)
print(student_name)
print(all_student)