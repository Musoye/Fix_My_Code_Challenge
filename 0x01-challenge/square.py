#!/usr/bin/python3
"""Defining the square class module"""


class Square():
    """Square class module"""
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """Intialization function"""
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
            if 'width' in kwargs.keys() and self.width != self.height:
                self.height = self.width
            if 'height' in kwargs.keys() and self.width != self.height:
                self.width = self.height

    def area(self):
        """ Area of the square """
        return self.width * self.width

    def Perimeter(self):
        """Perimeter of a Square"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """The print value"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print(s.area())
    print(s.Perimeter())
    print('___')
    b = Square(height=3)
    print(b)
    print(b.area())
    print(b.Perimeter())
    print('___')
    c = Square(width=5)
    print(c)
    print(c.area())
    print(c.Perimeter())
    print('___')
    d = Square()
    print(d)
    print(d.area())
    print(d.Perimeter())
