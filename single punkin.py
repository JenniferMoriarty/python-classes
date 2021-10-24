#pumpkin patch!
#version 1: draws a single punkin

import pygame
import math #needed to use pi
pygame.init()#initializes Pygame
pygame.display.set_caption("Pumpkins!")#sets the window title
screen = pygame.display.set_mode((800, 800))#creates game screen
screen.fill((0, 0, 0))#paint background black

#set up some colors
BLACK = (0,0,0)
ORANGE = (200, 100, 0)
GREEN = (0,150, 0)

pygame.draw.rect(screen, (GREEN), (190, 330, 20, 25)) #(190, 330) is my top left corner
pygame.draw.circle(screen, (ORANGE), (200, 400), 50) #(200, 400) is the center
pygame.draw.arc(screen, (BLACK), (185,400,30,20), math.pi, math.pi*2, 5) #(185, 400) is the top left corner of the box that the arc is drawn in
pygame.draw.arc(screen, (BLACK), (175,380,20,20), 0, math.pi, 5)
pygame.draw.arc(screen, (BLACK), (200,380,20,20), 0, math.pi, 5)

pygame.display.flip()
