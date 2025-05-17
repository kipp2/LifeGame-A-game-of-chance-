from app1 import *

class Demo(App):
    def __init__(self):
        super().__init__()

        scene0 = Scene()
        scene0.nodes.append(Text('Scene',pos =(20, 20)))
        scene0.nodes.append(Text('Introduction screen the app',pos =(20, 100)))

        scene1 =Scene (bg = Color('yellow'))
        scene1.nodes.append(Text('Scene 1', pos =(20, 20)))
        scene1.nodes.append(Text('Option Screen of the App', pos =(20, 100)))

        scene2 = Scene(bg=Color('green'))
        scene2.nodes.append(Text('Scene 2', pos =(20, 20)))
        scene2.nodes.append(Text('Main screen of the App', pos =(20, 100)))

        App.scene = App.scenes[0]

if __name__ == '__main__':
    Demo().run()