# Ab is code ka output predict karo:
class Parent:
    def show(self):
        print("Parent method")

class Child(Parent):
    def show(self):
        super().show()
        print("Child method")

c = Child()
c.show()

# Tumhare questions:
# 1. Output kya hoga aur kis order me?
# 2. Yahan super().show() kya kaam kar raha hai?

# Answer:
# 1. Parent method then Child method
# 2. It will call the parent class method