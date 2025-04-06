import pygame 
from pygame.locals import *

RED = (255, 0, 0)
GRAY = (127, 127, 127)

pygame.init()
w, h = 840, 440
size = w, h
screen = pygame.display.set_mode(size)
running = True

img = pygame.image.load('service2.png')
img.convert()
rect = img.get_rect()
rect.center = w//2, h//2
moving = False

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            
        elif event.type == MOUSEBUTTONDOWN:
            if rect.collidepoint(event.pos):
                moving = True

        elif event.type == MOUSEBUTTONUP:
            moving = False 

        elif event.type == MOUSEMOTION and moving:
                    rect.move_ip(event.rel)
    print(event)
    screen.fill(GRAY)
    screen.blit(img, rect)
    pygame.draw.rect(screen, RED, rect, 1)
    pygame.display.update()

pygame.quit()