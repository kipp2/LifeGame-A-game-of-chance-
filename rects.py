import pygame
from pygame.locals import *

SIZE = 500, 200
RED =(255, 0, 0)
GRAY = (150, 150, 150)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255,255, 0)
width, height = SIZE 
dir = {K_LEFT: (-5, 0), K_RIGHT: (5, 0), K_UP: (0, -5), K_DOWN: (0, 5)}

pygame.init()
screen = pygame.display.set_mode(SIZE)
font = pygame.font.Font(None, 14)

def update_screen():
    pygame.display.flip()
screen.fill(GRAY)

rect = Rect(50, 60, 200, 80)
print(f'x = {rect.x}, y = {rect.y}, w={rect.w}, h ={rect.h}')
print(f'left={rect.left}, top={rect.top}, right= {rect.right}, bottom={rect.bottom}')
print(f'center={rect.center} ')

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    pygame.draw.rect(screen, RED, rect)
    pygame.display.flip()
    break
