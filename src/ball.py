from typing import Any
import pygame

class Ball:
    def __init__(self, surface):
        self.__surface = surface
        self.__ballType = "green"
        self.__ballSize = 15
        self.__position = pygame.Vector2(surface.get_width()/2, surface.get_height()/2)
        
    
    def __setBall(self, ballType):
        self.__ballType = ballType

    def __getBall(self):
        return self.__ballType 
    def __setBallSize(self, ballSize):
        self.__ballSize = ballSize
    def __getBallSize(self):
        return self.__ballSize
    def __setSurface(self, surface):
        self.__surface = surface
    def __getSurface(self):
        return self.__surface

    def setPosition(self, newPos):
        self.__position = pygame.Vector2(newPos)
    def getPosition(self):
        return self.__position
    
    def drawBall(self):
        pygame.draw.circle(self.__getSurface(),self.__getBall(),self.getPosition(),self.__getBallSize())

    def collisionDetection(self):
        pass