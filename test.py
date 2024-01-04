import random, pygame, sys
from pygame.locals import *
 
Blue = (0,0,255)
Green = (0,255,0)
White = (255,255,255)
 
pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
DISPLAYSURF.fill(Blue)
pygame.display.set_caption('Sailing!')
 
FPS = 30
fpsClock = pygame.time.Clock()
 
Sail = pygame.Surface([100,10])
Sail.fill(White)
 
degrees = 0
 
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
 
    rotatedSail = pygame.transform.rotozoom(Sail, degrees, 1)
    Sail_rect = Sail.get_rect(topleft =(200,150))
    DISPLAYSURF.blit(rotatedSail, Sail_rect)
    pygame.display.flip()
 
    fpsClock.tick(FPS)
 
    degrees += 1