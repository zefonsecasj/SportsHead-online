import pygame

class Player:
    def __init__(self, surface):
        self.__name = "Ze"
        self.__playerType = "Red"
        self.__playerSize = pygame.Rect(((surface.get_width()/2, surface.get_height()/2),(50,50)))
        self.__position = pygame.Vector2(surface.get_width()/2, surface.get_height()/2)
        self.__isKicking = False
        self.__firstPlayer = True
        self.__surface = surface
        self.__PlayerSpeed = pygame.time.Clock().tick(60)/1000
        self.__SPEEDCONST = 100
        self.__jumping = False
        self.__gravity = 10
        self.__mass = 1
        self.PlayerBoot = boots("black", self.getSurface(), pygame.Vector2(self.getPosition().x,self.getPosition().y+50))

    def setPlayerName(self,name):
        self.__name = name
    def getPlayerName(self):
        return self.__name
    def setType(self, type):
        self.__playerType = type
    def getType(self):
        return self.__playerType
    def setPosition(self, newPos):
        self.__position = pygame.Vector2(newPos)
        self.__playerSize = pygame.Rect((self.getPosition(),(50,50)))
    def getPosition(self):
        return self.__position
    def setIsKicking(self, isKicking):
        self.__isKicking = isKicking
    def getIsKicking(self):
        return self.__isKicking
    def setPlayerSize(self, size):
        self.__playerSize = size
    def getSize(self):
        return self.__playerSize
    def __setSurface(self, newSurface):
        self.__surface = newSurface
    def getSurface(self):
        return self.__surface
    def __setSpeed(self, newSpeed):
        self.__PlayerSpeed = pygame.time.Clock().clock.tick(newSpeed)/1000
    def getPlayerSpeed(self):
        return self.__PlayerSpeed
    
    def enableJump(self):
        if(self.__jumping):
            force = (1/2)*self.__mass*(self.__gravity**2)
            self.setPosition((self.getPosition().x, self.getPosition().y - force))
            self.PlayerBoot.setBootPosition((self.PlayerBoot.getBootPosition().x, self.PlayerBoot.getBootPosition().y - force))
            self.__gravity -= 1
            if self.__gravity < 0:
                self.__mass = -1
            if self.__gravity == -11:
                self.__gravity = 10
                self.__mass = 1
                self.__jumping = False
        pygame.time.delay(15)

    def drawPlayer(self):
        pygame.draw.rect(self.getSurface(), self.getType(),self.getSize())
        self.PlayerBoot.drawBoot()

    def move(self):
        keys = pygame.key.get_pressed()
        self.enableJump()
        if(keys[pygame.K_w]):
            self.__jumping = True
        if(keys[pygame.K_a]):
            self.setPosition((self.getPosition().x - self.__SPEEDCONST*self.getPlayerSpeed(),self.getPosition().y))
            self.PlayerBoot.setBootPosition((self.PlayerBoot.getBootPosition().x - self.__SPEEDCONST*self.getPlayerSpeed(),self.PlayerBoot.getBootPosition().y))
        if(keys[pygame.K_d]):
            self.setPosition((self.getPosition().x + self.__SPEEDCONST*self.getPlayerSpeed(),self.getPosition().y))
            self.PlayerBoot.setBootPosition((self.PlayerBoot.getBootPosition().x + self.__SPEEDCONST*self.getPlayerSpeed(),self.PlayerBoot.getBootPosition().y))
        if(keys[pygame.K_SPACE]):
            self.PlayerBoot.kick()

class boots():
    def __init__(self, color, surface, playerPosition):
        self.color = color
        self.surface = surface
        self.bootSize = (40,20)
        self.boot = pygame.Rect(((surface.get_width()/2, surface.get_height()/2 + 50),(40,20)))
        self.bootPosition = playerPosition

    def getBootPosition(self):
        return self.bootPosition
    def setBootPosition(self, newPos):
        self.bootPosition = pygame.Vector2(newPos)
        self.boot = pygame.Rect((self.getBootPosition(),self.bootSize))

    def drawBoot(self):
        pygame.draw.rect(self.surface, self.color,self.boot)

    def kick(self):
        pass
            
        