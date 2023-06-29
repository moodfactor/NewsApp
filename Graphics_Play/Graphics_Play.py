from kivy.loader import Loader
from kivy.uix.image import AsyncImage
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.carousel import Carousel
from kivy.factory import Factory
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.atlas import Atlas
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Ellipse, Line, Rectangle
import cProfile
import kivy
kivy.require('1.9.0')


# define a string variable that contains the kv language code for the UI design
kv = """

<Myw>:

 

    
    
"""

# load the kv string into memory using Builder class
Builder.load_string(kv)


class MyW(BoxLayout):
    pass


class CustomLayout(FloatLayout):
    pass


class MyApp(App):

    def build(self):
        return Label (text='Hello[ref=world][color=0000ff]World[/color][/ref]',markup=True, font_size=80, font_name='DroidSans')

  


if __name__ == "__main__":
    MyApp().run()
