import pygame
pygame.init

#constants for colors
RED = (250,0,0)
ORANGE = (200, 100, 0)
GREEN = (0,150, 0)

# parent class
class Plant( object ):    
          
        def __init__(self, x, y):   
            self.xpos = x
            self.ypos = y
            self.size = 10
            self.water = 0
            
        def grow(self):
            if self.water>10:
                self.water-=10
                self.size +=20
                print("growing!")
                
        def getWatered(self):
            self.water+=5

  
# child class
class Flower( Plant ):           
        def __init__(self, xpos, ypos, type, color):
                self.color = color
                self.type = type
  
                # invoking the __init__ of the parent class 
                Plant.__init__(self, xpos, ypos)
        
        def draw(self):
            pygame.draw.rect(screen, (GREEN), (self.xpos-10, self.ypos+20, 20, 100+self.size*10)) 
            pygame.draw.circle(screen, (self.color), (self.xpos-20, self.ypos+20), 20+self.size) 
            pygame.draw.circle(screen, (self.color), (self.xpos-20, self.ypos-20), 20+self.size) 
            #add missing petals here
            pygame.draw.circle(screen, (ORANGE), (self.xpos, self.ypos), 20+self.size)         
                
  
                  
# creation of an object variable or an instance
f1 = Flower(200, 400, "daisy", RED)   

#creates game screen and caption
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("inheritance demo")

#game variables
doExit = False #variable to quit out of game loop
clock = pygame.time.Clock() #sets up a game clock to regulate game speed


#BEGIN GAME LOOP######################################################
while not doExit:
   
    clock.tick(60) #FPS (frames per second)
      
    #pygame's way of listening for events (key presses, mouse clicks, etc)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           doExit = True #lets you quit program

    #keyboard input-----------------------------------
    print("press w to water, any other key to skip")
    answer = input()
    if answer == 'w':
        f1.getWatered()
        print("watering plant!")
     
    #render section-----------------------------------
 

    #draw class objects
    f1.grow()
    f1.draw()

  

    pygame.display.flip() #update graphics each game loop

#END GAME LOOP#######################################################
pygame.quit()
