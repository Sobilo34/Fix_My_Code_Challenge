#!/usr/bin/python3
'''
Module suare
contains class square
'''


class Square():
    '''
    Class representing a square.

    Attributes:
    - width (int): The width of the square.
    - height (int): The height of the square.
    '''

    def __init__(self, *args, **kwargs):
        '''
        Initializes a square object with optional width and height.

        Parameters:
        - args: Positional arguments.
        - kwargs: Keyword arguments to set attributes.
        '''
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """
        Calculate the area of the square.

        Returns:
        - int: The area of the square.
        """
        return self.width * self.height

    def permiter_of_my_square(self):
        '''
        Calculate the perimeter of the square.

        Returns:
        - int: The perimeter of the square.
        '''
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        '''
        Return a string representation of the square.

        Returns:
        - str: A string representation of the square.
        '''
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    '''
    Test Class
    '''
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
