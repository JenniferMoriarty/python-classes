import pygame #import library (called "modules" in python)
from math import sin #so we don't have to type "math.sin" each time
from math import cos

pygame.init()#initializes Pygame
pygame.display.set_caption("Valentine's Hearts")#sets the window title
screen = pygame.display.set_mode((800, 800))#creates game screen
screen.fill((0, 0, 0))#paint background black

GameLoop = True #variable to run game loop

xpos = 0
ypos = 0
t=0
ticker = 2
adder = 1
# GAME LOOP-----------------------------------------------------------
while GameLoop:
    if ticker<1 or ticker>250:
        adder*=-1
    ticker+=adder
    t+=1
    xpos=-100*2.5 *sin(t)+100*.8*sin(3*t)-100*.5*cos(36*t/7)+400
    ypos = -100*2.7*cos(t)+100*cos(2*t)+100*.5*cos(3*t)-100*.5*sin(36*t/7)+400
    pygame.draw.circle(screen, (250, ticker, ticker), (xpos, ypos), 2)
    pygame.display.flip()
pygame.quit()
