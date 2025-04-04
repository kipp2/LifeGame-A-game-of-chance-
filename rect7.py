from rects import *

moving = False

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type ==MOUSEBUTTONDOWN:
            if rect.collidepoint(event.pos):
                moving = True

        elif event.type == MOUSEBUTTONUP:
            moving = False
        
        elif event.type == MOUSEMOTION and moving:
            rect.move_ip(event.rel)
            if rect.left < 0:
                rect.right += width
            elif rect.right > width:
                rect.left -= width
    screen.fill(GRAY)
    pygame.draw.rect(screen, RED, rect)
    if moving:
        pygame.draw.rect(screen, BLUE, rect, 4)
    pygame.display.flip()
pygame.quit()