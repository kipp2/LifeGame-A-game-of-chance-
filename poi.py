from rects import *





pts = ('topleft', 'topright', 'bottomleft', 'bottomright',
       'midtop', 'midright', 'midbottom', 'midleft', 'center')



running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False 
        else:
              print(event)        
          
    screen.fill(GRAY)
    pygame.draw.rect(screen, GREEN, rect, 4)
    for pt in pts:
        pos = eval ('rect.'+pt)
        draw_text(pt, pos[0], pos[1])
        pygame.draw.circle(screen, RED, pos, 3)

    update_screen()

pygame.quit()