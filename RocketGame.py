import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH , HEIGHT))
pygame.display.set_caption("Rocket Game")

Rocket = pygame.draw.rect(screen,"White",(400,300,50,100))


gameloop = True
while gameloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False

    screen.fill("darkblue")
    Rocket = pygame.draw.rect(screen,"White",(400,300,50,100))
    pygame.display.flip()

pygame.quit()