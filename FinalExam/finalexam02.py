import math

class Point:
    x = 0
    y = 0


    def __init__(self, input_x, input_y):
        x = input_x
        y = input_y


    def __distance__(self, other):
        sqrt(pow(self.x - other.x, 2) + pow(self.y - other.y, 2)


    def __add__(self, other):
        result = (self.x + other.x, self.y + other.y)


if __name__ = "__main__":
    a = Point(2, 2);
    b = Point(1, 1);

    print(({}).format(a + b))