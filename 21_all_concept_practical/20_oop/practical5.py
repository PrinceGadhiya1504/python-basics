from abc import ABC
class BankAccount:
    bank_name = "ABC Bank"

    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name


account = BankAccount("Amit", 5000)

print(account.owner)
print(account.get_balance())
print(account.bank_name)

BankAccount.change_bank_name("XYZ Bank")
print(account.bank_name)

# questions:
# 1. Complete output kya hoga?
# 2. __balance ke aage double underscore __ kyun use kiya hai?
# 3. @classmethod aur cls ka kya role hai?
# 4. self aur cls me kya difference hai?

# Answer
# 1. Amit, 5000, ABC Bank, XYZ Bank
# 2. __ sign use to make variable private and make it name harder to access from out side of the class
# 3. A class method is a method that works with the class rather than a specific object. We use the @classmethod decorator to define it, and cls refers to the class itself.
# 4. self is used to refer instance of class and cls is used to refer class