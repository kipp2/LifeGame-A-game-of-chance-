from rects import *
import random 

def random_rect(n):
    rect_width = 60
    rect_height = 30
    return [
        pygame.Rect(
            random.randint(0, width - 60), 
            random.randint(0, height- 30), 
            rect_width, 
            rect_height
        )
        for _ in range(n)
    ]


rects = random_rect(50)

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_r:
                rects = random_rect(50)

    screen.fill(GRAY)
    pygame.draw.rect(screen, GREEN, rect, 1)
    for r in rects:
        if rect.colliderect(r):
            pygame.draw.rect(screen, RED, r, 2)
        else:
            pygame.draw.rect(screen, BLUE, r, 1)
    pygame.display.flip()

pygame.quit()