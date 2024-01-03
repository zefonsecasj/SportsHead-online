import pygame
from src import ball, player

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((1260,640))

    player_pos = pygame.Vector2(screen.get_width()/2, screen.get_height()/2)

    clock = pygame.time.Clock()
    running = True
    dt = 0

    newBall = ball.Ball(screen)
    newPlayer = player.Player(screen)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill("purple")
        newBall.drawBall()
        newPlayer.drawPlayer()
        
        newPlayer.move()
        
        pygame.display.update()


        dt = clock.tick(60)/1000

    pygame.quit()