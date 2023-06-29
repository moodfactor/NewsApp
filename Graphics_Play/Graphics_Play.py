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

    def _image_loaded(self, proxyImage):
        if proxyImage.image.texture:
            self.image.texture = proxyImage.image.texture

    def build(self):
        proxyImage = Loader.image(
            "https://images.pexels.com/photos/842711/pexels-photo-842711.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1")
        proxyImage.allow_stretch = True
        proxyImage.keep_ratio = False
        proxyImage.anim_delay = 0.1
        proxyImage.anim_loop = True
        proxyImage.anim_repeat = True
        proxyImage.loading_image = "R.png"
        proxyImage.error_image = "R.png"
        proxyImage.bind(on_load=self._image_loaded)
        proxyImage.bind(on_error=self._image_loaded)
        self.image = AsyncImage()
        return self.image


if __name__ == "__main__":
    MyApp().run()
