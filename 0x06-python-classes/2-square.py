#!/usr/bin/python3
'''A class with size'''
class Square:
    '''Defines a square'''
    def __init__(self, size):
        '''initializing a new attribute size which is private'''
        self.__size = size
        '''validation of size'''
        self.__validate_size()
    '''Define another method'''
    def __validate_size(self):
        if not isinstance(self.__size, int):
            '''raise an error if size is not an integer'''
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            '''raise an error if size is less than zero'''
            raise ValueError("size must be >= 0")
