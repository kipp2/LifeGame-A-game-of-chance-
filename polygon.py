import pygame
from pygame.locals import *

size = 960, 640
width, height = size 
pygame.init()

GRAY = (127, 127, 127)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
screen = pygame.display.set_mode(size)

running = True 
start = (0, 0)
drawing = False
points = []
while running:  
    for event in pygame.event.get():
        if event.type == QUIT:
            running == False
        elif event.type == MOUSEBUTTONDOWN:
            points.append(event.pos)
            drawing = True
        elif event.type == MOUSEBUTTONUP:
            drawing = False
        elif event.type == MOUSEMOTION and drawing:
            points[-1] = event.pos
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                if len(points)>0:
                    points.pop()

        screen.fill(GRAY)
        if len(points)>1:
            rect = pygame.draw.lines(screen, RED, True, points, 3)
            pygame.draw.rect(screen, GREEN, rect, 1)
        pygame.display.update()

pygame.quit()

        


