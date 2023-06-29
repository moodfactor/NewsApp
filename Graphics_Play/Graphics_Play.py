import cProfile
from kivy.graphics import Color, Ellipse, Line
from kivy.uix.floatlayout import FloatLayout
from kivy.atlas import Atlas
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.factory import Factory
from kivy.uix.carousel import Carousel
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.app import App
import kivy
kivy.require('1.9.0')


# define a string variable that contains the kv language code for the UI design
kv = """


    
    
"""

# load the kv string into memory using Builder class
Builder.load_string(kv)


class MyW(Widget):

    def on_touch_down(self, touch):
        with self.canvas:
            Color(1, 1, 0)
            d = 30.
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            touch.ud['line'] = Line(points=(touch.x, touch.y))

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]


class CustomLayout(FloatLayout):
    pass


class MyApp(App):

    def on_start(self):
        print("on_start")
        self.profile = cProfile.Profile()
        self.profile.enable()

    def on_stop(self):
        print("on_stop")
        self.profile.disable()
        s = self.profile.print_stats()
        # save s to file s.profile on disk
        self.profile.dump_stats("s.profile")
    def build(self):
        return MyW()


if __name__ == "__main__":
    MyApp().run()
