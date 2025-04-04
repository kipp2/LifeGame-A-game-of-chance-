from rects import * 

rect = Rect(100, 50, 50, 50)
x, y = 1, 1
v = (x, y)

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    rect.move_ip(v)

    if rect.left < 0:
        x *= -1
    if rect.right > width:
        x *= -1
    if rect.top < 0:
        y *= -1
    if rect.bottom > height:
        y *= -1
    
    screen.fill(GRAY)
    pygame.draw.rect(screen, RED, rect )
    pygame.display.flip()
pygame.quit()