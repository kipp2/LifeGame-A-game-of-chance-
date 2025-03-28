import pygame
from pygame.locals import * 
import random 

YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
background = GRAY
size = 940, 620
width, height = size 
pygame.init()

screen = pygame.display.set_mode(size)
color = [YELLOW, CYAN, MAGENTA, BLACK, GRAY, WHITE, RED, GREEN, BLUE]

ball_radius =20
ball_color = BLUE
ball_pos = [width // 2, height //2]
ball_speed = [3, 3]

running = True
clock = pygame.time.Clock()

while running:
    
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            ball_color = random.choice(color)
    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]
    
    if ball_pos[0] - ball_radius < 0 or ball_pos[0] + ball_radius > width:
        ball_speed[0] = -ball_speed[0]
    if ball_pos[1] - ball_radius < 0 or ball_pos[1] + ball_radius > height:
        ball_speed[1] = -ball_speed[1]
        
    screen.fill(GREEN )
    pygame.draw.circle(screen, ball_color, ball_pos, ball_radius)
    pygame.display.update()
    clock.tick(60)
pygame.quit()

