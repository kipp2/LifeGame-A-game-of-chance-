from rects import * 

rect0 = rect.copy()
    
v = (0,0)


while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key in dir:
                v = dir[event.key]
                rect.inflate_ip(v)
    
    screen.fill(GRAY)
    pygame.draw.rect(screen, BLUE, rect0, 1)
    pygame.draw.rect(screen, RED, rect, 4)
    pygame.display.flip()

pygame.quit()