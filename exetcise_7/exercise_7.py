from math import sqrt, pi


class Figure:
    def dimention(self):
        raise NotImplementedError

    def perimeter(self):
        return None

    def square(self):
        return None

    def squareSurface(self):
        return None

    def squareBase(self):
        return None

    def height(self):
        return None

    def volume(self):
        raise NotImplementedError

    def __str__(self):
        params = ", ".join(f"{k}={v}" for k, v in self.__dict__.items())
        return f"{self.__class__.__name__}({params})"


# --- 2D Фігури ---
class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def dimention(self):
        return 2

    def perimeter(self):
        return self.a + self.b + self.c

    def square(self):
        if (self.a + self.b <= self.c) or (self.a + self.c <= self.b) or (self.b + self.c <= self.a):
            return 0

        s = self.perimeter() / 2
        return sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def volume(self):
        return self.square()


class Rectangle(Figure):
    def __init__(self, a, b):
        self.a, self.b = a, b

    def dimention(self):
        return 2

    def perimeter(self):
        return 2 * (self.a + self.b)

    def square(self):
        return self.a * self.b

    def volume(self):
        return self.square()


class Trapeze(Figure):
    def __init__(self, a, b, c, d):
        self.a, self.b, self.c, self.d = a, b, c, d

    def dimention(self):
        return 2

    def perimeter(self):
        return self.a + self.b + self.c + self.d

    def square(self):
        base_diff = abs(self.b - self.a)
        if base_diff == 0:
            return 0
        expr = self.c ** 2 - (((base_diff) ** 2 + self.c ** 2 - self.d ** 2) / (2 * base_diff)) ** 2
        if expr < 0:
            return 0
        h = sqrt(expr)
        return ((self.a + self.b) / 2) * h

    def volume(self):
        return self.square()


class Parallelogram(Figure):
    def __init__(self, a, b, h):
        self.a, self.b, self.h = a, b, h

    def dimention(self):
        return 2

    def perimeter(self):
        return 2 * (self.a + self.b)

    def square(self):
        return self.a * self.h

    def volume(self):
        return self.square()


class Circle(Figure):
    def __init__(self, r):
        self.r = r

    def dimention(self):
        return 2

    def perimeter(self):
        return 2 * pi * self.r

    def square(self):
        return pi * self.r ** 2

    def volume(self):
        return self.square()


# --- 3D Фігури ---
class Ball(Figure):
    def __init__(self, r):
        self.r = r

    def dimention(self):
        return 3

    def squareSurface(self):
        return 4 * pi * self.r ** 2

    def volume(self):
        return (4 / 3) * pi * self.r ** 3


class TriangularPyramid(Triangle):
    def __init__(self, a, h):
        super().__init__(a, a, a)  # правильний трикутник
        self.h = h

    def dimention(self):
        return 3

    def squareBase(self):
        return super().square()

    def height(self):
        return self.h

    def volume(self):
        return (1 / 3) * self.squareBase() * self.h


class QuadrangularPyramid(Rectangle):
    def __init__(self, a, b, h):
        super().__init__(a, b)
        self.h = h

    def dimention(self):
        return 3

    def squareBase(self):
        return super().square()

    def height(self):
        return self.h

    def volume(self):
        return (1 / 3) * self.squareBase() * self.h


class RectangularParallelepiped(Rectangle):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c

    def dimention(self):
        return 3

    def squareBase(self):
        return super().square()

    def height(self):
        return self.c

    def squareSurface(self):
        return 2 * (self.a * self.b + self.b * self.c + self.a * self.c)

    def volume(self):
        return self.a * self.b * self.c


class Cone(Circle):
    def __init__(self, r, h):
        super().__init__(r)
        self.h = h

    def dimention(self):
        return 3

    def squareBase(self):
        return super().square()

    def height(self):
        return self.h

    def squareSurface(self):
        l = sqrt(self.r ** 2 + self.h ** 2)  # твірна конуса
        return pi * self.r * l + self.squareBase()

    def volume(self):
        return (1 / 3) * self.squareBase() * self.h


class TriangularPrism(Triangle):
    def __init__(self, a, b, c, h):
        super().__init__(a, b, c)
        self.h = h

    def dimention(self):
        return 3

    def squareBase(self):
        return super().square()

    def height(self):
        return self.h

    def squareSurface(self):
        return self.perimeter() * self.h + 2 * self.squareBase()

    def volume(self):
        return self.squareBase() * self.h


# --- Створення фігур ---
def create_figure(name, params):
    if name == "Triangle":
        return Triangle(*map(float, params))
    elif name == "Rectangle":
        return Rectangle(*map(float, params))
    elif name == "Trapeze":
        return Trapeze(*map(float, params))
    elif name == "Parallelogram":
        return Parallelogram(*map(float, params))
    elif name == "Circle":
        return Circle(*map(float, params))
    elif name == "Ball":
        return Ball(*map(float, params))
    elif name == "TriangularPyramid":
        return TriangularPyramid(*map(float, params))
    elif name == "QuadrangularPyramid":
        return QuadrangularPyramid(*map(float, params))
    elif name == "RectangularParallelepiped":
        return RectangularParallelepiped(*map(float, params))
    elif name == "Cone":
        return Cone(*map(float, params))
    elif name == "TriangularPrism":
        return TriangularPrism(*map(float, params))
    else:
        raise ValueError(f"Unknown figure: {name}")


def main():
    figures = []
    with open("/Users/anastasianosko/PycharmProjects/practics/exetcise_7/input03.txt", "r") as file:
        for line in file:
            parts = line.strip().split()
            if not parts:
                continue
            name, params = parts[0], parts[1:]
            fig = create_figure(name, params)
            if fig.volume() is not None:
                figures.append(fig)

    if not figures:
        print("Немає фігур з обчислюваним обсягом.")
        return

    max_figure = max(figures, key=lambda f: f.volume())

    with open("output3.txt", "w") as f:
        f.write("Фігура з найбільшою мірою:\n")
        f.write(str(max_figure) + "\n")
        f.write(f"Значення міри: {max_figure.volume()}\n")



if __name__ == "__main__":
    main()
