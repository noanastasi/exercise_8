from math import sqrt, pi

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        if self.a + self.b <= self.c or self.a + self.c <= self.b or self.b + self.c <= self.a:
            return 0
        s = self.perimeter() / 2
        return sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))


class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def perimeter(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.b


class Trapeze:
    def __init__(self, a, b, c, d):
        self.a = a  # основа 1
        self.b = b  # основа 2
        self.c = c  # бічна 1
        self.d = d  # бічна 2

    def perimeter(self):
        return self.a + self.b + self.c + self.d

    def area(self):
        try:
            base_diff = self.b - self.a
            if base_diff == 0:
                return 0
            h = sqrt(self.c ** 2 - (((base_diff) ** 2 + self.c ** 2 - self.d ** 2) / (2 * base_diff)) ** 2)
            return ((self.a + self.b) / 2) * h
        except:
            return 0


class Parallelogram:
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h

    def perimeter(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.h


class Circle:
    def __init__(self, r):
        self.r = r

    def perimeter(self):
        return 2 * pi * self.r

    def area(self):
        return pi * self.r**2


def create_figure(line):
    parts = line.strip().split()
    shape = parts[0]
    params = list(map(float, parts[1:]))

    if shape == "Triangle":
        return Triangle(*params)
    elif shape == "Rectangle":
        return Rectangle(*params)
    elif shape == "Trapeze":
        return Trapeze(*params)
    elif shape == "Parallelogram":
        return Parallelogram(*params)
    elif shape == "Circle":
        return Circle(*params)
    else:
        return None


def main():
    figures = []
    with open("/Users/anastasianosko/PycharmProjects/practics/6/input03.txt", "r") as file:
        for line in file:
            fig = create_figure(line)
            if fig:
                figures.append(fig)

    max_area_fig = max(figures, key=lambda f: f.area())
    max_perimeter_fig = max(figures, key=lambda f: f.perimeter())

    with open("output03.txt", "w") as out:
        out.write(f"Figure with max area: {type(max_area_fig).__name__}, area = {max_area_fig.area():.2f}\n")
        out.write(f"Figure with max perimeter: {type(max_perimeter_fig).__name__}, perimeter = {max_perimeter_fig.perimeter():.2f}\n")


if __name__ == "__main__":
    main()
