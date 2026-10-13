# 1. Shape naam ki abstract class banao, jisme area() abstract method ho.
# 2. Rectangle class ko Shape se inherit karao aur constructor me width aur height set karo.
# 3. area() method override karke rectangle ka area return karo.
# 4. @staticmethod se description() method banao, jo "This is a rectangle" return kare.
# 5. @property se area ko property ke roop me expose karo, taaki rectangle.area likhkar area mile.
# 6. __str__() define karo, jo rectangle ki width aur height ko readable format me return kare.
# 7. Rectangle(10, 5) ka object banao aur area, description aur object print karo.
# Expected output:
# Area: 50
# This is a rectangle
# Rectangle(width=10, height=5)

from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    @staticmethod
    def description():
        return "This is a rectangle"

    @property
    def area(self):
        return self.calculate_area()

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


r1 = Rectangle(10, 5)
print(f"Area: {r1.area}")
print(r1.description())
print(r1)

        