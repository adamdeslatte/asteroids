import pygame

class Bullet:

    def __init__(self, position, orientation):
        self.__position = position
        self.__orientation = orientation
    
    def get_position(self):
        return self.__position

    def get_orientation(self):
        return self.__orientation

    def set_position(self, position):
        self.__position = position

    def set_orientation(self,orientation):
        self.__orientation = orientation

    def get_rect(self):
        return pygame.Rect(self.__position[0],self.__position[1],3,3)
    