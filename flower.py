#pygame flowers!
#draws a simple flower made of basic shapes to a game window

import pygame #gaming module (aka library) 
pygame.init() #initializes Pygame
pygame.display.set_caption("flowers!") #sets the window title
screen = pygame.display.set_mode((800, 800)) #creates game screen
screen.fill((0, 0, 0)) #paint background black

#set up some colors
RED = (250,0,0)
ORANGE = (200, 100, 0)
GREEN = (0,150, 0)

#here are the shapes getting drawn
pygame.draw.rect(screen, (GREEN), (190, 220, 20, 100)) #(190, 330) is my top left corner
pygame.draw.circle(screen, (RED), (180, 220), 20) 
pygame.draw.circle(screen, (RED), (180, 180), 20) 
pygame.draw.circle(screen, (RED), (220, 220), 20) 
pygame.draw.circle(screen, (RED), (220, 180), 20) 
pygame.draw.circle(screen, (ORANGE), (200, 200), 20) 


pygame.display.flip() #this flips all those shapes onto the game screen (needed for every game)
