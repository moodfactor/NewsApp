import kivy
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

# define a string variable that contains the kv language code for the UI design
kv = """

<CustomLayout>:
    # define a canvas instruction that draws a yellow rectangle before the widget content
    canvas.before:
        Color:
            # set the color to yellow (red, green, blue, alpha)
            rgba: 1, 1, 0, 1
        Rectangle: 
            # set the position of the rectangle to the widget
            pos: self.pos
            # set the size of the rectangle to the widget size
            size: self.size

 # define a rule for MyW widget, which is a subclass of BoxLayout
<MyW>:
    CustomLayout:
    
        # add an AsyncImage widget as a child of CustomLayout widget,
        # which loads an image asynchronously from a source
        AsyncImage:
            source: '11.png'
            size_hint: 1, .5
            pos_hint: {'center_x': .5, 'center_y': .5}
            
    AsyncImage:
        source: '22.png'

    # add another CustomLayout widget as a child of MyW widget
    CustomLayout:
        AsyncImage:
            source: '33.png'
            size_hint: 1, .5
            pos_hint: {'center_x': .5, 'center_y': .5}
    
    
"""

# load the kv string into memory using Builder class 
Builder.load_string(kv)


class MyW(BoxLayout):
    pass


class CustomLayout(FloatLayout):
    pass


class MyApp(App):
    def build(self):
        return MyW()


if __name__ == "__main__":
    MyApp().run()
