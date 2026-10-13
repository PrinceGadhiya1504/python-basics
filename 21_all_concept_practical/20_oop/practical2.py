# Ab predict karo ki is code ka output kya hoga:

class Parent:
    def show(self):
        print("Parent method")

class Child(Parent):
    def show(self):
        print("Child method")

c = Child()
c.show()

# Tumhare questions:
# 1. Output kya hoga?
# 2. Parent class me bhi show() method hai aur Child class me bhi. Phir kaunsa method execute hoga, aur kyun?

# Answer
# 1. Child method
# 2. Because of in child class inharit parent class so when we call c.show() then it will go to child class
#    and execute show() method and also same method so override the parent class method in child class