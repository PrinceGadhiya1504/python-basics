# Code ko dhyan se dekho aur output predict karo:

class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def sound(self):
        print(f"{self.name} barks")


dog = Dog("Tommy", "Labrador")

print(dog.name)
print(dog.breed)
dog.sound()
print(isinstance(dog, Dog))
print(isinstance(dog, Animal))

# Tumhare 3 questions:
# 1. Is code ka complete output kya hoga?
# 2. super().__init__(name) ki zaroorat kyun padi?
# 3. isinstance(dog, Animal) ka result True hoga ya False, aur kyun?

# Answer
# 1. Tommy, Labrador, Tommy barks, True, True
# 2. super().__init__(name) is used to call the parent class constructor
# 3. True because of Dog class inharit Animal class