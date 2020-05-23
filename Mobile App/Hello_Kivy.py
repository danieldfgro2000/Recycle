import kivy
from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.label import Label

class MainApp(App):
    def build(self):
        # label = Label(text='Hello from Kivy',
        #               size_hint=(.5, .5),
        #               pos_hint={'center_x': .5, 'center_y': .5})



        img = Image(source='../elephant_gray.jpeg',
                size_hint=(1, .5),
                pos_hint={'center_x': .5, 'center_y': .5})

        return img

if __name__ == '__main__':
    app = MainApp()
    app.run()