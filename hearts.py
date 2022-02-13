import pygame #import library (called "modules" in python)
from math import sin #so we don't have to type "math.sin" each time
from math import cos

pygame.init()#initializes Pygame
pygame.display.set_caption("Valentine's Hearts")#sets the window title
screen = pygame.display.set_mode((800, 800))#creates game screen
screen.fill((0, 0, 0))#paint background black

GameLoop = True #variable to run game loop


# GAME LOOP-----------------------------------------------------------
while GameLoop:
    
    #draws a heart using lines and arcs
    pygame.draw.arc(screen, (250, 0, 0), (400, 400, 40, 40), 0, 3.14,5)
    pygame.draw.arc(screen, (250, 0, 0), (360, 400, 40, 40), 0, 3.14,5)
    pygame.draw.line(screen, (250, 0, 0), (362, 420), (400, 475), 5)
    pygame.draw.line(screen, (250, 0, 0), (400, 475), (437, 420), 5)
    
    #draws a heart using circles and triangles
    pygame.draw.circle(screen, (250, 100, 100), (200, 200), 21)
    pygame.draw.circle(screen, (250, 100, 100), (240, 200), 21)
    pygame.draw.polygon(screen, (250, 100, 100), ((180, 205), (260, 205), (220, 250)))
    
    pygame.display.flip()
pygame.quit()

