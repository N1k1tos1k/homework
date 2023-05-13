class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def square(self):
        return self.width * self.height

rectangle = Rectangle(5, 10)

print(rectangle.square())