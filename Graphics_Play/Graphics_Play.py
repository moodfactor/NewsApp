import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.carousel import Carousel
from kivy.factory import Factory
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


kv = """

    
    
"""

Builder.load_string(kv)


class MyW(BoxLayout):
    def __init__(self, **kwargs):
        super(MyW, self).__init__(**kwargs)
        carousel = Carousel(direction='right')
        for i in range(3):
            src = f"f{i}.jpg"
            image = Factory.AsyncImage(source=src)
            carousel.add_widget(image)
            carousel.add_widget(Button(text=f"Button{i}"))

        self.add_widget(carousel)


class MyApp(App):
    def build(self):
        return MyW()


if __name__ == "__main__":
    MyApp().run()
