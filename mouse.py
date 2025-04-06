import pygame 
from pygame.locals import *

GRAY = (127, 127, 127)
RED = (255, 0, 0)

size = 960, 640
width, height = size 
pygame.init()

screen = pygame.display.set_mode(size)

running = True 
start = (0, 0)
size = (0, 0)
drawing = False
rectangles = []
rect_list = []

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False 
        elif event.type == KEYDOWN:
            if event.key == K_r:
                rectangles.clear()             
        elif event.type == MOUSEBUTTONDOWN:
            start = event.pos
            size = 0, 0
            drawing = True 
        elif event.type == MOUSEBUTTONUP:
            end = event.pos
            x1, y1 = start
            x2, y2 = end
            start = (min(x1, x2), min(y1, y2))
            size = (abs(x2 - x1), abs(y2 - y1))
            rect = pygame.Rect(start, size)
            rectangles.append((start, size))
            drawing = False 
        elif event.type == MOUSEMOTION and drawing:
            end = event.pos
            x1, y1 = start
            x2, y2 = end
            start = (min(x1, x2), min(y1, y2))
            size = (abs(x2 - x1), abs(y2 - y1))
            
        screen.fill(GRAY)
        for rect in rectangles and rect_list:
            pygame.draw.rect(screen, RED, (*rect[0], *rect[1]), 2)
            if drawing: 
                pygame.draw.rect(screen, RED, (start,size), 2)
        pygame.display.update()
        
pygame.quit()
