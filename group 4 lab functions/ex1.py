from math import pi

def circumference_of_circle(radius):
    circumference = 2 * pi * radius
    print(f"Circumference of the circle is {round(circumference, 3)}")

def area_of_circle(radius):
    area = pi * radius ** 2
    print(f"Area of the circle is {round(area, 3)}")

radius = float(input('enter the radius of the circle: '))

circumference_of_circle(radius)
area_of_circle(radius)

    
