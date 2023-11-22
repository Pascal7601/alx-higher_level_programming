#!/usr/bin/python3
'''A class with size'''
class Square:
    '''Defines a square'''
    def __init__(self, size=0, position=(0, 0)):
        '''using the property setter to set the size'''
        self.size = size
        '''using the property setter to set the position'''
        self.position = position  
        self.__validate_size()
        self.__validate_position()

    '''property'''
    @property
    def size(self):
        return self.__size
    
    '''uses setter function'''
    @size.setter
    def size(self, value):
        self.__size = value
        self.__validate_size()

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value
        self.__validate_position()

    '''Define another method'''
    def __validate_size(self):
        if not isinstance(self.__size, int):
            '''raise an error if size is not an integer'''
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            '''raise an error if size is less than zero'''
            raise ValueError("size must be >= 0")
    '''Defines a new method'''
    def __validate_position(self):
        if not isinstance(self.__position, tuple) or len(self.__position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(isinstance(coord, int) and coord >= 0 for coord in self.__position):
            raise ValueError("position must be a tuple of 2 positive integers")
        

    '''Defines new method area'''
    def area(self):
        '''returns area of the square'''
        return self.__size ** 2
    
    '''Defines a new method'''
    def my_print(self):
        '''checks if size is zero'''
        if self.__size == 0:
            print()
        else:

            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
