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

class Scene:
    id = 0 
    bg = Color('gray')
    def __init__(self, *args, **kwargs):
        App.scenes.append(self)
        App.scene = self
            
        self.id = Scene.id
        Scene.id += 1
        self.nodes = []
        self.bg = Scene.bg

        
    def draw(self):
        App.screen.fill(self.bg)
        for node in self.nodes:
            node.draw()
            pygame.display.flip()
        
    def __str__(self):
        return 'Scene {}'.format(self.id)


class App:
    
    def __init__(self):
        pygame.init()
        self.flags = RESIZABLE
        self.rect = Rect(0,0, 640, 240)
        App.screen = pygame.display.set_mode(self.rect.size, self.flags)
        App.t = Text('pygame App', pos =(20, 20))
        App.scenes = []
        
        self.scene = Scene()
        self.scene.nodes.append(App.t)

        App.running = True
        self.shortcuts = {
            (K_x, KMOD_LMETA): 'print("cmod+X")', 
            (K_x, KMOD_LALT): 'print("alt+X)',
            (K_x, KMOD_LCTRL): 'print("ctr+X)', 
            (K_x, KMOD_LMETA + KMOD_LSHIFT): 'print(cmod+shift+X)', 
            (K_x, KMOD_LMETA + KMOD_LALT): 'print(cmod+alt+X)',
            (K_x, KMOD_LMETA + KMOD_LALT + KMOD_LSHIFT): 'print("cmd+alt+shift+x)',
            (K_f, KMOD_LMETA): 'self.toggle_fullscreen()', 
            (K_r, KMOD_LMETA): 'self.toggle_resizable()',
            (K_g, KMOD_LMETA): 'self.toggle_frame()',
        }
    
    def do_shortcut(self, event):
        k = event.key
        m = event.mod
        if (k, m) in self.shortcuts:
            exec(self.shortcuts[k, m])

    def toggle_fullscreen(self):
        self.flags = FULLSCREEN
        pygame.display.set_mode(self.rect.size, self.flags)

    def toggle_resizable(self):
        self.flags = RESIZABLE
        pygame.display.set_mode(self.rect.size, self.flags)

    def toggle_frame(self):
        self.flags = NOFRAME
        pygame.display.set_mode(self.rect.size, self.flags)
        

    def run(self):
        
        while App.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    App.running = False 

                if event.type == KEYDOWN:
                    self.do_shortcut(event)
                    if event.key == K_s:
                        print("key press s")

        

            self.scene.draw
            pygame.display.update()

        pygame.quit()

if __name__ == '__main__':
    App().run()
