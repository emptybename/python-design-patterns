"""
We are not initializing Bitmap until draw_image being called by adding proxy in between
"""


class Bitmap:
    def __init__(self, filename):
        self.filename = filename
        print(f'Loading image {self.filename}')

    def draw(self):
        print(f'Drawing image {self.filename}')


class LazyBitmap:
    def __init__(self, filename):
        self.filename = filename
        self._bitmap = None

    def draw(self):
        if self._bitmap is None:
            self._bitmap = Bitmap(self.filename)
        self._bitmap.draw()


def draw_image(image):
    print('About to draw image')
    image.draw()
    print('Drawing done')


if __name__ == '__main__':
    image = LazyBitmap('facepalm.png')
    draw_image(image)
    draw_image(image)
