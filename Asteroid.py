import random
import pygame

class Asteroid:

    def __init__(self, size, position):
        self.__size = size
        self.__position = position
        self.__orientation = random.randint(0,360)
        self.__velocity = random.randint(1,3)

    def get_size(self):
        return self.__size
    
    def get_position(self):
        return self.__position

    
    def get_orientation(self):
        return self.__orientation

    def get_velocity(self):
        return self.__velocity

    def set_velocity(self, velocity):
        self.__velocity = velocity

    def set_position(self, position):
        self.__position = position

    def get_rect(self):
        return pygame.Rect(self.__position[0],self.__position[1], self.__size * 25, self.__size * 25)

    def break_asteroid(self):
        if self.__size > 1:
            return [Asteroid(self.__size - 1,self.__position),Asteroid(self.__size - 1,self.__position)]
        else:
            self.__size = 0
            return []
    