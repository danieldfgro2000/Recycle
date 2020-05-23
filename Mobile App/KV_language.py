from kivy.app import App
from kivy.uix.button import Button

class ButtonApp(App):
    def build(self):
        text: 'Press me'
        size_hint: (.5, .5)
        pos_hint: {'center_x': .5, 'center_y': .5}
        on_press: app.on_press_button()
        return Button()

    def on_press_button(self):
        print('You pressed the button!')

if __name__ == '__main__':
    app = ButtonApp()
    app.run()