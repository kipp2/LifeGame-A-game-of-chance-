from rects import *

rect0 = Rect(50, 60, 200, 80)
rect = rect0.copy()
dir = {K_LEFT: (-5, 0), K_RIGHT: (5, 0), K_UP: (0, -5), K_DOWN: (0, 5)}
v = (0,0)


while running:    
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key in dir:
                v=dir[event.key]
                
    new_x = rect.left + v[0]
    new_y = rect.top + v[1]

    if 0 <= new_x <= width - rect.width:
        rect.left = new_x
    if 0 <= new_y <= height - rect.height:
        rect.top = new_y

    v = (0,0)

            

    screen.fill(GRAY)
    pygame.draw.rect(screen, BLUE, rect0, 1)
    pygame.draw.rect(screen, RED, rect, 4)
    pygame.display.flip()

pygame.quit()


        