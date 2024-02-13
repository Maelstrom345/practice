import math


def area(radius):
   area = radius * radius *math.pi
   return area
radius = float(input("enter the radius of the circle: "))
print(f"the area of the circle is {area(radius)}")