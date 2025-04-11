import pygame 
from pygame.locals import *

class Text:

    def __init__(self, text, pos, **options):
        self.text = text
        self.pos = pos 

        self.fontname = None
        self.fontsize = 72
        self.fontcolor = Color('black')
        self.set_font()
        self.render()

    def set_font(self):
        self.font = pygame.font.Font(self.fontname, self.fontsize)

    def render(self):
        self.img = self.font.render(self.text, True, self.fontcolor)
        self.rect = self.img.get_rect()
        self.rect.topleft = self.pos

    def draw(self):
        App.screen.blit(self.img, self.rect)

class App:
    
    def __init__(self):
        pygame.init()
        flags = RESIZABLE 
        App.screen = pygame.display.set_mode((640, 240), flags)
        App.t = Text('pygame App', pos =(20, 20))

        App.running = True

    def run(self):
        
        while App.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    App.running = False 

            App.screen.fill(Color('gray'))
            App.t.draw()
            pygame.display.update()

        pygame.quit()

if __name__ == '__main__':
    App().run()
