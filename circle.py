import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius

# Example usage:
radius = 5
my_circle = Circle(radius)

area_of_circle = my_circle.area()
perimeter_of_circle = my_circle.perimeter()

print(f"Radius of the circle: {radius}")
print(f"Area of the circle: {area_of_circle:.2f}")
print(f"Perimeter of the circle: {perimeter_of_circle:.2f}")
