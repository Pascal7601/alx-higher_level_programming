#!/usr/bin/python3
'''A class with size'''
class Square:
    '''Defines a square'''
    def __init__(self, size=0):
        '''initializing a new attribute size which is private'''
        self.__size = size
        '''validation of size'''
        self.__validate_size()
    '''property'''
    @property
    def size(self):
        return self.__size
    
    '''uses setter function'''
    @size.setter
    def size(self, value):
        self.__size = value
        self.__validate_size()


    '''Define another method'''
    def __validate_size(self):
        if not isinstance(self.__size, int):
            '''raise an error if size is not an integer'''
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            '''raise an error if size is less than zero'''
            raise ValueError("size must be >= 0")
    '''Defines new method area'''
    def area(self):
        '''returns area of the square'''
        return self.__size ** 2
