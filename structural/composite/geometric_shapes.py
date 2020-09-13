"""
Treat all geographic objects same, either single or group of objects
Its like Trie Data structure
"""


class GraphicObject:
    def __init__(self, color=None):
        self.color = color
        self.children = []
        self._name = "Group"

    @property
    def name(self):
        return self._name

    def _print(self, items, depth):
        items.append('*' * depth)
        if self.color:
            items.append(self.color)
        items.append(f'{self.name}\n')
        for child in self.children:
            child._print(items, depth + 1)

    def __str__(self):
        items = []
        self._print(items, 0)
        return ''.join(items)


class Circle(GraphicObject):
    @property
    def name(self):
        return "Circle"


class Square(GraphicObject):
    @property
    def name(self):
        return "Square"


if __name__ == '__main__':
    drawing = GraphicObject()
    drawing._name = 'My Drawing'
    drawing.children.append(Circle('Red'))
    drawing.children.append(Square('Blue'))
    drawing1 = GraphicObject()
    drawing1.children.append(Circle('Yellow'))
    drawing1.children.append(Square('Green'))
    drawing1.children.append(drawing)
    print(drawing1)
