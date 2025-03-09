class Shape:
    def perimeter(self):
        pass

    def area(self):
        pass

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        if self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
            s = self.perimeter() / 2
            area = s * (s - self.a) * (s - self.b) * (s - self.c)
            return area ** 0.5 if area >= 0 else 0
        else:
            return 0

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height

class Trapeze(Shape):
    def __init__(self, base1, base2, side1, side2):
        self.base1 = base1
        self.base2 = base2
        self.side1 = side1
        self.side2 = side2

    def perimeter(self):
        return self.base1 + self.base2 + self.side1 + self.side2

    def area(self):
        try:
            if self.base1 == self.base2 or self.base1 <= 0 or self.base2 <= 0:
                return 0
            term1 = (self.side1 ** 2) - ((((self.base2 - self.base1) ** 2) + (self.side1 ** 2) - (self.side2 ** 2)) / (
                        2 * (self.base2 - self.base1))) ** 2
            if term1 < 0:
                return 0

            height = term1 ** 0.5
            return (self.base1 + self.base2) * height / 2
        except (ValueError, ZeroDivisionError):
            return 0

class Parallelogram(Shape):
    def __init__(self, base, side, height):
        self.base = base
        self.side = side
        self.height = height

    def perimeter(self):
        return 2 * (self.base + self.side)

    def area(self):
        return self.base * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return 2 * 3.14159 * self.radius

    def area(self):
        return 3.14159 * self.radius ** 2

def read_shapes(file_name):
    shapes = []
    with open(file_name, 'r') as file:
        for line in file:
            parts = line.split()
            if not parts:
                continue
            name = parts[0]
            params = []
            for value in parts[1:]:
                params.append(float(value))
            if name == "Triangle" and len(params) == 3:
                shapes.append(Triangle(params[0], params[1], params[2]))
            elif name == "Rectangle" and len(params) == 2:
                shapes.append(Rectangle(params[0], params[1]))
            elif name == "Trapeze" and len(params) == 4:
                shapes.append(Trapeze(params[0], params[1], params[2], params[3]))
            elif name == "Parallelogram" and len(params) == 3:
                shapes.append(Parallelogram(params[0], params[1], params[2]))
            elif name == "Circle" and len(params) == 1:
                shapes.append(Circle(params[0]))
    return shapes

def find_max_shapes(shapes):
    max_area_shape = shapes[0]
    for shape in shapes:
        if shape.area() > max_area_shape.area():
            max_area_shape = shape

    max_perimeter_shape = shapes[0]
    for shape in shapes:
        if shape.perimeter() > max_perimeter_shape.perimeter():
            max_perimeter_shape = shape

    return max_area_shape, max_perimeter_shape

if __name__ == "__main__":
    shapes = read_shapes("input01.txt")
    max_area_shape, max_perimeter_shape = find_max_shapes(shapes)

    print(f"Фігура з найбільшою площею: {type(max_area_shape).__name__}, площа: {max_area_shape.area():.2f}")
    print(
        f"Фігура з найбільшим периметром: {type(max_perimeter_shape).__name__}, периметр: {max_perimeter_shape.perimeter():.2f}")