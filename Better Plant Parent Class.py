import pygame

# Initialize Pygame
pygame.init()

# Constants for colors
RED = (250, 0, 0)
ORANGE = (200, 100, 0)
GREEN = (0, 150, 0)

# Parent class
class Plant:
    def __init__(self, x, y):   
        self.__xpos = x
        self.__ypos = y
        self.__size = 10
        self.__water = 0

    def grow(self):
        if self.__water > 10:
            self.__water -= 10
            self.__size += 20
            print("Growing!")

    def get_watered(self):
        self.__water += 5

# Child class
class Flower(Plant):
    def __init__(self, xpos, ypos, type, color):
        self.color = color
        self.type = type
        super().__init__(xpos, ypos)
    
    def draw(self, screen):
        pygame.draw.rect(screen, GREEN, (self.__xpos - 10, self.__ypos + 20, 20, 100 + self.__size * 10))
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (i, j) != (0, 0):
                    pygame.draw.circle(screen, self.color, (self.__xpos + i * 20, self.__ypos + j * 20), 20 + self.__size)
        pygame.draw.circle(screen, ORANGE, (self.__xpos, self.__ypos), 20 + self.__size)

# Game setup
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Inheritance Demo")
clock = pygame.time.Clock()
f1 = Flower(200, 400, "Daisy", RED)
do_exit = False

# Game loop
while not do_exit:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            do_exit = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                f1.get_watered()
                print("Watering plant!")

    f1.grow()
    screen.fill((255, 255, 255))  # Clear screen
    f1.draw(screen)
    pygame.display.flip()

pygame.quit()
