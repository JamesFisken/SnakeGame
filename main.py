import sys

import pygame
from pygame.locals import *

pygame.init()

fps = 60
fpsClock = pygame.time.Clock()

width, height = 1000, 1000
grid_width = 40
grid_height = 40
screen = pygame.display.set_mode((width, height))
squares = []
class square():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.square_size = 20
        self.snake = False
    def display(self):
        print(self.x, self.y)
        a = 20
        b = 20
        r = 10
        if (self.x + self.y) % 2 == 1:
            pygame.draw.rect(screen, (0, 200, 0), pygame.Rect(self.x * self.square_size, self.y * self.square_size, self.square_size - 1, self.square_size - 1))
        else:
            pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(self.x * self.square_size, self.y * self.square_size, self.square_size - 1,self.square_size - 1))






for x in range(grid_width):
    for y in range(grid_height):
        squares.append(square(x, y))


# Game loop.
while True:


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

      #creates green background
    for sq in squares:
        sq.display()

    pygame.display.flip()
    fpsClock.tick(fps)