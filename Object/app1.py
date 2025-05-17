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
    default_bg = Color('gray')
    def __init__(self,bg = None,  *args, **kwargs):
        App.scenes.append(self)
        App.scene = self
            
        self.id = Scene.id
        Scene.id += 1
        self.nodes = []
        self.bg = bg if bg else Scene.default_bg

        
    def draw(self):
        App.screen.fill(self.bg)
        for node in self.nodes:
            node.draw()
            
        
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
            (K_x, KMOD_LALT): 'print("alt+X")',
            (K_x, KMOD_LCTRL): 'print("ctr+X")', 
            (K_x, KMOD_LMETA + KMOD_LSHIFT): 'print("cmod+shift+X")', 
            (K_x, KMOD_LMETA + KMOD_LALT): 'print("cmod+alt+X")',
            (K_x, KMOD_LMETA + KMOD_LALT + KMOD_LSHIFT): 'print("cmd+alt+shift+x")',
            (K_f, KMOD_LMETA): 'self.toggle_fullscreen()', 
            (K_r, KMOD_LMETA): 'self.toggle_resizable()',
            (K_g, KMOD_LMETA): 'self.toggle_frame()',
        }
    
    def do_shortcut(self, event):
        for (key, mod), action in self.shortcuts.items():
            if event.key == key and (event.mod & mod) == mod:
                exec(action)
                break

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
                    elif event.key == K_RIGHT:
                        i = current_index = App.scenes.index(App.scene)
                        App.scene = App.scenes[(i + 1) % len(App.scenes)]
                    elif event.key == K_LEFT:
                        current_index = App.scenes.index(App.scene)
                        App.scene = App.scenes[(i -1) % len(App.scenes)]        


            App.scene.draw()
            pygame.display.update()

        pygame.quit()


