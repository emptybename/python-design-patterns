from abc import ABC


class Shape(ABC):
    def __str__(self):
        return ''


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def resize(self, factor):
        self.radius *= factor

    def __str__(self):
        return f'Circle with radius {self.radius}'


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def resize(self, factor):
        self.side *= factor

    def __str__(self):
        return f'Square of side {self.side}'


# Decorators

class ColorShape(Shape):
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color

    def __str__(self):
        return f'{self.shape} of color {self.color}'


class TransparentShape(Shape):
    def __init__(self, shape, transparency):
        self.shape = shape
        self.transparency = transparency

    def __str__(self):
        return f'{self.shape} with transparency {self.transparency*100} %'


if __name__ == '__main__':
    circle = Circle(5)
    print(circle)
    red_circle = ColorShape(circle, 'red')
    print(red_circle)

    transparent_circle = TransparentShape(circle, .5)
    print(transparent_circle)
    transparent_red_circle = TransparentShape(red_circle, .8)
    print(transparent_red_circle)

    # But There is one problem that we cant restrict -
    print(ColorShape(ColorShape(circle, 'red'), 'blue'))

    # Also we can't call red_circle.resize()
