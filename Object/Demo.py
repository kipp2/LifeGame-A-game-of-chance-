from app1 import *

class Demo(App):
    def __init__(self):
        super().__init__()

        Scene(caption = 'Intro')
        Text('Scene',pos =(20, 20))
        Text('Introduction screen the app',pos =(20, 20))

        Scene (bg = Color('yellow'), caption = "Option")
        Text('Scene 1', pos =(20, 20))
        Text('Option Screen of the App', pos =(20, 20))

        Scene(bg=Color('green'), caption = 'Main' )
        Text('Scene 2', pos =(20, 20))
        Text('Main screen of the App', pos =(20, 20))

        App.scene = App.scenes[0]

if __name__ == '__main__':
    Demo().run()