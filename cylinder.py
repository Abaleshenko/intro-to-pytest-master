from math import pi


class Cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def full_area(self):
        return 2 * pi * self.radius * (self.radius + self.height)

    def volume(self):
        return pi * self.radius ** 2 * self.height


if __name__ == "__main__":
    c = Cylinder(4, 8)
    print(f"Площадь полной поверхности: {round(c.full_area(), 2)}")
    print(f"Объём: {round(c.volume(), 2)}")









class Cube:
    def __init__(self, side):
        self.side = side

    def area(self):
        return 6 * self.side ** 2

    def volume(self):
        return self.side ** 3


if __name__ == "__main__":
    c = Cube(5)
    print(f"Площадь полной поверхности куба: {c.area()}")
    print(f"Объём куба: {c.volume()}")



