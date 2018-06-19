from kivy.app import App
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

class clockApp (App):
    pass


if __name__ == '__main__':
    Window.clearcolor = get_color_from_hex('#101216')
    clockApp().run()
