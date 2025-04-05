from rects import *
import random

n = 30
def random_rects(n):
    rect_width = 40
    rect_height = 30
    return [
        Rect(
            random.randint(0, width - rect_width),
            random.randint(0, height - rect_height), 
            rect_width, 
            rect_height
        )
        for _ in range(n)
    ]
rects = random_rects(n)

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if event.type == KEYDOWN:
            if event.type == K_r:
                rects = random_rects(30)

    screen.fill(GRAY)
    intersecting = []
    for i in range(n-1):
        r0 = rects[i]
        for j in range(i+1, n):
            r1 = rects[j]
            if r0.colliderect(r1):
                intersecting.append(r0)
                intersecting.append(r1)
                break

    for i, r in enumerate(rects):
        color = RED if r in intersecting else BLUE
        pygame.draw.rect(screen,color, r)
        draw_text(str(i), r.topleft, r.topleft)

    pygame.display.flip()
pygame.quit()