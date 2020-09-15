class TextFormatted:
    def __init__(self, text):
        self.text = text
        self.caps = [False] * len(self.text)

    def capitalize(self, start, end):
        for i in range(start, end + 1):
            self.caps[i] = True

    def __str__(self):
        chars = []
        for i in range(len(self.text)):
            c = self.text[i].upper() if self.caps[i] else self.text[i]
            chars.append(c)
        return ''.join(chars)


class BetterTextFormatted:
    def __init__(self, plane_text):
        self.plane_text = plane_text
        self.format_range = []

    class TextRange:
        def __init__(self, start, end, capitalize=False):
            self.start = start
            self.end = end
            self.capitalize = capitalize

        def covers(self, position):
            return self.start <= position <= self.end

    def range(self, start, end):
        text_range = self.TextRange(start, end)
        self.format_range.append(text_range)
        return text_range

    def __str__(self):
        chars = []
        for i in range(len(self.plane_text)):
            c = self.plane_text[i]
            for r in self.format_range:
                if r.covers(i) and r.capitalize:
                    c = c.upper()
            chars.append(c)
        return ''.join(chars)


if __name__ == '__main__':
    text = TextFormatted('This is a new brave world')
    text.capitalize(14, 19)
    print(text)

    text = BetterTextFormatted('This is a new brave world')
    text.range(3, 6).capitalize = True
    print(text)
