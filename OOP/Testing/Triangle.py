from copy import copy
class triangle:

    def __init__(self, a, b, c):
        assert a + b > c and a + c > b and b + c > a
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def square(self):
        p = self.perimeter() / 2.0
        sq = p * (p - self.a) * (p - self.b) * (p - self.c)
        return sq ** 0.5

##### main #####

tr = triangle(3, 4, 5)

print(f"Площа трикутника = {tr.square()}")

#print("Площа заданого трикутника = %f" % tr.square())

tr_copy = copy(tr)

print(f"tr: {tr.a, tr.b, tr.c}")
print(f"tr_copy: {tr_copy.a, tr_copy.b, tr_copy.c}")

tr_copy.b = 99

print(f"tr: {tr.a, tr.b, tr.c}")
print(f"tr_copy: {tr_copy.a, tr_copy.b, tr_copy.c}")