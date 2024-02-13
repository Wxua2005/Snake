import pygame
import sys
from constants import WIDTH , HEIGHT , FPS , VERTICAL , HORIZONTAL
from Engine import Gamestate

pygame.init()   # initialising pygame
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH,HEIGHT)) # screen 
screen.fill('Brown')
running = True
Gamestate = Gamestate(screen)  # Creating a Gamestate object

while running:
    Gamestate.body()   # Function responsible for drawing the snake body
    Gamestate.food()
    Gamestate.eating()

    """
    Moving position state

    D : Right
    A : Left
    W : Up
    S : Down
    """
    if pygame.key.get_pressed()[pygame.K_a]:
        if Gamestate.orientation != HORIZONTAL:
            Gamestate.swaphorizontal()
        Gamestate.moveleft()
    if pygame.key.get_pressed()[pygame.K_d]:
        if Gamestate.orientation != HORIZONTAL:
            Gamestate.swaphorizontal()
        Gamestate.moveright()
    if pygame.key.get_pressed()[pygame.K_w]:
        if Gamestate.orientation != VERTICAL:
            Gamestate.swapvertical()
        Gamestate.moveup()
    if pygame.key.get_pressed()[pygame.K_s]:
        if Gamestate.orientation != VERTICAL:
            Gamestate.swapvertical()
        Gamestate.movedown()
    
    for event in pygame.event.get(): # Game loop
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_ESCAPE: # Close if a pressed
                print(Gamestate.score)
                running = False
            if event.key == pygame.K_g:  # Growth size 
                Gamestate.growth()

    clock.tick(FPS)
    pygame.display.update() # Updating the display
    screen.fill('Brown')
pygame.quit()
