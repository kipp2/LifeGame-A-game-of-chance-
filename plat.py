import pygame
import random

# Initialize Pygame
pygame.init()

# Game Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
GRAVITY = 0.5
SCROLL_THRESH = 200

# Create Game Window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platformer Game")

# Player Class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 60))  # Player size
        self.image.fill(BLUE)  # Blue color
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 100)  # Start position

        # Movement attributes
        self.vel_x = 0
        self.vel_y = 0
        self.on_ground = False
        self.score = 0

    def update(self):
        # Apply gravity
        self.vel_y += GRAVITY
        
        # Move the player
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y        

        self.on_ground = False
        for platform in platforms:
            if self.rect.colliderect(platform.rect) and self.vel_y > 0:
                self.rect.bottom = platform.rect.top
                self.vel_y = 0
                self.on_ground = True

        if self.rect.top <= SCROLL_THRESH:
            for platform in platforms:
                platform.rect.y += abs(self.vel_y)
            self.rect.y += abs(self.vel_y)
            self.score += 1

        # Prevent player from falling below screen
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
            self.vel_y = 0
            self.on_ground = True

    def move(self, direction):
        if direction == "left":
            self.vel_x = -5
        elif direction == "right":
            self.vel_x = 5
        
        if self.rect.right < 0:
            self.rect.left = WIDTH
        elif self.rect.left >= WIDTH:
            self.rect.right = 0
    

    def stop(self):
        self.vel_x = 0

    def jump(self):
        if self.on_ground:
            self.vel_y = -12
            self.on_ground = False
            
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

def generate_platforms():
    platforms = [Platform(200, HEIGHT -50, 400, 20)]
    for i in range(6):
        x = random.randint(100, WIDTH - 200)
        y = HEIGHT - (i * 100) - 50
        platforms.append(Platform(x, y, 200, 20))
    return platforms

# Create player instance
player = Player()

platforms = generate_platforms()

# Game Loop
clock = pygame.time.Clock()
running = True

while running:
    clock.tick(FPS)
    screen.fill(WHITE)  # Clear screen

    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle Key Presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.move("left")
    elif keys[pygame.K_RIGHT]:
        player.move("right")
    else:
        player.stop()

    if keys[pygame.K_SPACE]:
        player.jump()

    # Update and Draw Player
    player.update()
    screen.blit(player.image, player.rect)

    platforms = [p for p in platforms if p.rect.top < HEIGHT]

    if len(platforms) < 6:
        x = random.randint(100, WIDTH - 200)
        y = platforms[-1].rect.top - 100
        platforms.append(Platform(x, y, 200, 20))
        
    
    for platform in platforms:
        screen.blit(platform.image, platform.rect)

    pygame.display.update()

pygame.quit()

