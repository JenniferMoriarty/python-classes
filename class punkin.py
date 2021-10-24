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

class Punkin:#-----------------------------------------------------------------------------
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos

    def draw(self):
        pygame.draw.rect(screen, (GREEN), (self.xpos-10, self.ypos-70, 20, 25)) #(190, 330) is my top left corner
        pygame.draw.circle(screen, (ORANGE), (self.xpos, self.ypos), 50) #(200, 400) is the center
        pygame.draw.arc(screen, (BLACK), (self.xpos-15,self.ypos,30,20), math.pi, math.pi*2, 5) #(185, 400) is the top left corner of the box that the arc is drawn in
        pygame.draw.arc(screen, (BLACK), (self.xpos-25,self.ypos-20,20,20), 0, math.pi, 5)
        pygame.draw.arc(screen, (BLACK), (self.xpos,self.ypos-20,20,20), 0, math.pi, 5)
#end class punkin---------------------------------------------------------------------------
    
#instantiate a few punkins:
Jack = Punkin(100, 400)
p2 = Punkin(400, 200)

Jack.draw()
p2.draw()

pygame.display.flip()
