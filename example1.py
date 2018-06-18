from kivy.app import App
from kivy.uix.button import Button

class TurorialApp(App):
    def build(self):
        return Button(text = "Hello World!", background_color=(0,0,1,1), font_size=50)

if __name__ == "__main__":
    TurorialApp().run()
