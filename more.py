import pygame 
from pygame.locals import *
import random 

RED = (255, 0, 0)
GREEN = (0, 250, 0)
BLUE = (0, 0, 250)
GRAY = (127, 127, 127)

size = 640, 320
width, height = size 
pygame.init()

background = GRAY 
running = True 

screen = pygame.display.set_mode(size)
screen.fill(GRAY)

def position():
    pos_x, pos_y = random.randint(0,640), random.randint(0, 320)
    return pos_x, pos_y

pos = position()
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    screen.fill(GRAY)

    pygame.draw.rect(screen, RED, (pos[0],pos[1], 170, 100))
    pygame.draw.rect(screen, GREEN, (100, 60, 120, 100))
    pygame.draw.rect(screen, BLUE, (150, 100, 120, 100))
    pygame.draw.rect(screen, RED, (350, 20, 120, 100), 1)
    pygame.draw.rect(screen, GREEN, (400, 60, 120, 100), 4)
    pygame.draw.rect(screen, BLUE, (450, 100, 120, 100), 8)

    pygame.display.update()

pygame.quit()
    

