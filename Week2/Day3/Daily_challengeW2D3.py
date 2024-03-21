import math
class Circle:
    def __init__(self,radius):
        self.radius = radius

    def creating_circle(self):
        area = (math.pi * (self.radius** 2))
        print(f"The area of the circle is equal to {area}")

    def __str__(self):
        output = f'''{self.radius} is the radio of the circle'''
        return output
    def __add__(self,other):
        if isinstance(other, Circle):
            new_circle = (math.pi * ((self.radius + other.radius)**2))
            return print(f"The new circle out of both circles will be {new_circle}")

    def __eq__(self,other):
        if isinstance(other,Circle):
            if (self.radius*2) > (other.radius*2):
                return print(f"{self.radius} is bigger than {other.radius}")
            elif (self.radius*2) == (other.radius*2):
                return print(f"{self.radius} is equal to {other.radius}")

        return print(False)

c1 = Circle(5)
c2 = Circle(10)
c3 = Circle(1)

c1.creating_circle()
print(c1)
print(c1+c2)
print(c2==c1)
circle_list = [c1,c2,c3]
sorted_circle = sorted(circle_list, key=lambda x: x.radius)
for circle in sorted_circle:
    print(circle)


import turtle
t = turtle.Turtle()

r=10
t.circle(r)


