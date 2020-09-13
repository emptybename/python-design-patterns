"""
Draw different shapes in different renderer like
Draw circle in vector or raster, draw square in vector or raster same for triangle.....
so we do this by splitting 2 different concepts shapes and renderer and connect them using bridge.
"""
from abc import ABC


class Renderer(ABC):
    def render_circle(self, radius):
        pass


class VectorRenderer(Renderer):
    def render_circle(self, radius):
        print("Drawing Circle of radius {}".format(radius))


class RasterRenderer(Renderer):
    def render_circle(self, radius):
        print("Drawing Circle in pixel of radius {}".format(radius))


class Shape(ABC):
    def __init__(self, renderer):
        self.renderer = renderer  # Connecting Two components

    def draw(self): pass

    def resize(self, factor): pass


class Circle(Shape):
    def __init__(self, renderer, radius):
        super(Circle, self).__init__(renderer)
        self.radius = radius

    def draw(self):
        self.renderer.render_circle(self.radius)

    def resize(self, factor):
        self.radius = self.radius * factor


"""
if We want to add square then we have to add square class and add render_square in Renderer interface. 
Same for other shape
"""

if __name__ == "__main__":
    vector_renderer = VectorRenderer()
    raster_renderer = RasterRenderer()
    circle = Circle(vector_renderer, 5)
    circle.draw()
    circle1 = Circle(raster_renderer, 10)
    circle1.draw()
