import pygame

class Player:

    def __init__(self, position, orientation,size):
        self.__position = position
        self.__orientation = orientation
        self.__velocity = 0
        self.__size = size
    
    def set_position(self, position):
        self.__position = position

    def add_orientation(self, orientation):
        self.__orientation += orientation
    
    def add_velocity(self, velocity):
        self.__velocity += velocity

    def get_position(self):
        return self.__position

    def get_orientation(self):
        return self.__orientation
    
    def get_velocity(self):
        return self.__velocity

    def get_rect(self):
        return pygame.Rect(self.__position[0],self.__position[1], self.__size[0], self.__size[1])