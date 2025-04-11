import pygame
from pygame.locals import * 
import time

BLACK = (0,0,0)
RED = (255, 0, 0)
GREEN = (0, 0, 255)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)
w, h = 640, 240
size = w, h 

pygame.init()
screen = pygame.display.set_mode(size)

sysfont = pygame.font.get_default_font()
print('system font :', sysfont)

t0 = time.time()
font = pygame.font.SysFont(None, 48)
print('time needed for font creation', time.time()- t0)

img = font.render(sysfont, True, RED)
rect = img.get_rect()
pygame.draw.rect(img, BLUE, rect, 1)

font1 = pygame.font.SysFont('notosansnabataean', 72)
img1 = font1.render('notosansnabataean', True, BLUE)

font2 = pygame.font.SysFont('notosansogham', 72)
img2 = font2.render('notosansogham', True, GREEN)

fonts = pygame.font.get_fonts()
print(len(fonts))
for i in range(7):
    print(fonts[i])

running = True
background = GRAY
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    screen.fill(background)
    screen.blit(img, (20, 20))
    screen.blit(img1, (20, 50))
    screen.blit(img2, (20, 20))
    pygame.display.update()

pygame.quit()