# Ye code dekho aur bina run kiye output predict karo:

class Parent:
    def show(self):
        print("Parent show method")

class Child(Parent):
    def display(self):
        print("Child display method")

c = Child()
c.display()
c.show()

# Tumhe 2 questions ke answer dene hain:
# 1. Output kya aayega aur kis order me?
# 2. Child class me show() method define nahi hai, phir bhi c.show() kaise execute hoga?

# Answer
# 1. Child display method then Parent show method because  Child class inherit Parent class and first call child method
# 2. Because of in child class inharit parent class so when we call c.show() then it will go to parent class and execute show() method