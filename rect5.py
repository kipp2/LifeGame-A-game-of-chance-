import pygame 
from pygame.locals import *

Size = 800, 600
RED = (255, 0, 0)
BLUE = (0, 255, 0)
GREEN = (0, 0, 255)
GRAY = (127, 127, 127)
width, height= Size


pygame.init()
dir = {K_LEFT: (-5, 0), K_RIGHT: (5, 0), K_UP: (0, -5), K_DOWN: (0, 5)}
v = (0,0)



screen = pygame.display.set_mode(Size)
rect = Rect(50, 60, 200, 80)
rect0 = Rect(50, 60, 200, 80)

rect0 = rect.copy()
screen.fill(GRAY)

running = True 
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type ==KEYDOWN:
            if event.key in dir:
                v = dir[event.key]
                rect.inflate_ip(v)


    screen.fill(GRAY)
    pygame.draw.rect(screen, BLUE, rect0, 1)
    pygame.draw.rect(screen, RED, rect, 4)
    pygame.display.flip()

pygame.quit()