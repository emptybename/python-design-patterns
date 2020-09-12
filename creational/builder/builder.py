"""
Create any HTML element using builder outsourcing
"""


class HTMLElement:
    indent_size = 2

    def __init__(self, name='', text=''):
        self.name = name
        self.text = text
        self.elements = []

    def __str(self, indent):
        lines = []
        i = ' ' * (indent * self.indent_size)
        lines.append(f'{i}<{self.name}>')

        if self.text:
            i1 = ' ' * ((indent + 1) * self.indent_size)
            lines.append(f'{i1}{self.text}')

        for e in self.elements:
            lines.append(e.__str(indent + 1))

        lines.append(f'{i}</{self.name}>')
        return '\n'.join(lines)

    def __str__(self):
        return self.__str(0)

    @staticmethod
    def create(name):
        return HTMLBuilder(name)


class HTMLBuilder:
    def __init__(self, root_name):
        self.root_name = root_name
        self.__root = HTMLElement(root_name)

    # Not Fluent
    def add_child(self, name, text):
        self.__root.elements.append(
            HTMLElement(name, text)
        )

    # Fluent
    def add_child_fluent(self, name, text):
        self.__root.elements.append(
            HTMLElement(name, text)
        )
        return self

    def __str__(self):
        return str(self.__root)


if __name__ == "__main__":

    builder = HTMLElement.create('ul')
    builder.add_child('li', 'Hello')
    builder.add_child('li', 'World')
    print(builder)

    # Fluent way of creating html-elements
    builder1 = HTMLElement.create('ul')
    builder1.add_child_fluent('li', 'Hello')\
        .add_child_fluent('li', 'World')
    print(builder1)
