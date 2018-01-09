from math import pi
radius = float(input("What is the radius of your circle?"))
def find_circumference(radius):
    """Returns the circumference of a circle"""
    c = 2 * pi * radius
    return c
print("The circumference of your circle is", find_circumference(radius), "when the radius is", radius)


def find_area(radius):
    """Returns the area of a circle"""
    a = pi * radius ** 2
    return a
print("The area of your circle is", find_area(radius), "when the radius is", radius)

radius = float(input("What is the radius of your sphere?"))

def find_surface_area(radius):
    """Returns the surface area of a sphere"""
    sa = 4 * pi * radius ** 2
    return sa
print("The surface area of your sphere is", find_surface_area(radius), "when the radius is", radius)