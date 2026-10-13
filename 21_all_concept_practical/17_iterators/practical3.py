# Ek class MyEnumerate banao jo:
# 1. __init__(self, items) mein list store kare aur index 0 se start kare.
# 2. __iter__() mein iterator khud return kare.
# 3. __next__() mein current index aur item ka tuple return kare, jaise (0, "Apple").
# 4. Har call par index increment kare.
# 5. List ke saare elements khatam hone par StopIteration raise kare.
# 6. for loop se iterator ke saare results print kare.
# 7. list(MyEnumerate(fruits)) se complete result list banao.

# Expected output
# (0, 'Apple')
# (1, 'Banana')
# (2, 'Mango')
# (3, 'Orange')
# [(0, 'Apple'), (1, 'Banana'), (2, 'Mango'), (3, 'Orange')]

fruits = ["Apple", "Banana", "Mango", "Orange"]

class MyEnumerate:
    def __init__(self, items):
        self.index = 0
        self.items = items
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < len(self.items):
            result = (self.index, self.items[self.index])
            self.index += 1
            return result
        else:
            raise StopIteration

# Test 1: for loop se iterator ke saare results print kare
for item in MyEnumerate(fruits):
    print(item)

# Test 2: list(MyEnumerate(fruits)) se complete result list banao
print(list(MyEnumerate(fruits)))
        