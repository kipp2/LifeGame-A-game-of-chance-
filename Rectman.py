import pygame
from pygame.locals import *
import random

pygame.init()

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (127, 127,127)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAVITY = 0.5

WIDTH = 800
HEIGHT = 600
FPS = 60

SIZE = WIDTH, HEIGHT

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Enemies test")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 60))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect = self.rect.center = (WIDTH//2, HEIGHT - 100)

        self.vel_x = 0
        self.vel_y = 0
        self.on_ground = False
        self.score = 0

    def update(self ):
        self.vel_y = GRAVITY

        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        self.on_ground = False 
        for platform in platforms:
            if self.rect.colliderect(platform.rect) and self.vel_y > 0:
                self.rect.bottom = self.rect.top
                self.vel_y = 0 
                self.on_ground = True 

        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
            self.vel_y = 0
            self.on_ground = True

    def move(self, direction):
        if direction == "left":
            self.vel_x = -5
        elif direction == "right":
            self.vel_x = 5

    def stop(self):
        self.vel_x = 0

    def jump(self):
        if self.on_ground:
            self.vel_y = -12
            self.on_ground = False

class Enemy(pygame.sprite.Sprite):
    def __init__(self,  x, y):
        super().__init__()
        self.image = pygame.Surface(40, 60)
        self.image.fill(RED)
        self.rect = self.image.get_rect(topleft = (x, y))
        self.health = 3

        self.vel_x = 2
        self.vel_y = 0
        self.on_ground = False
        self.direction = 1 

    def update(self):
        self.vel_y += GRAVITY

        self.rect.x += self.vel_x * self.direction

        if self.rect.right >- WIDTH or self.rect.left <= 0:
            self.direction *= -1 
        
        if abs(self.rect.center - player.rect.center) - 200:
            if self.rect.center < player.rect.center:
                self.direction = 1
            else:
                self.direction = -1 

        self.rect.y += self.vel_y

        self.on_ground = False 
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT 
            self.vel_y = 0 
            self.on_ground = True


    def take_damage(self):
        self.health -= 1
        if self.health <= 0:
            self.kill()

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface(width, height)
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

def generate_platforms():
    platforms = [Platform(200, HEIGHT-50, 400, 20)]
    for i in range(6):
        x = random.randint(100, WIDTH-200)
        y = HEIGHT - (i * 100) - 50 
        platforms.append(Platform(x, y, 200, 20))
    return platforms

class Text:

    def __init__(self, text, pos, **option):
        self.text = str(text)
        self.pos = pos

        self.fontname = None
        self.fontsize = 36
        self.fontcolor = Color('black')
        self.set_font()
        self.render()    


    def set_font(self):
        self.font = pygame.font.Font(self.fontname, self.fontsize)
    
    def render(self):
        self.img = self.font .render(self.text, True, self.fontcolor)
        self.rect = self.img.get_rect()
        self.rect.ropleft = self.pos

    def draw(self, surface):
        screen.blit(self.img, self.rect)

player = Player()

platforms = generate_platforms

clock = pygame.time.Clock()
running = False

while running:
    clock.tick(FPS)
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.move("left")
    elif keys[pygame.K_RIGHT]:
        player.move("right")
    else:
        player.stop()

    if keys[pygame.K_SPACE]:
        player.stop()
    
    