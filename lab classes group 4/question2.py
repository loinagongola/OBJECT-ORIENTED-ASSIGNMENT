from math import pi

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area = pi * (self.radius ** 2)
        print(f"The area of the circle is: {area}")

    def perimeter(self):
        perimeter = 2 * pi * self.radius
        print(f"The perimeter of the circle is: {perimeter}")

my_circle = Circle(5)
my_circle.area()
my_circle.perimeter()
