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


kv = """

    
    
"""

Builder.load_string(kv)


class MyW(BoxLayout):
    def __init__(self, **kwargs):
        super(MyW, self).__init__(**kwargs)

        # To create atlas do in terminal: python -m kivy.atlas myatlas 642 *.png
        # myatlas is the name of the atlas
        # 642 is the size of the images
        # *.png is the file type of the images
        
        btn = Button(text='', background_normal='atlas://myatlas/11',
                     background_down='atlas://myatlas/33')
        self.add_widget(btn)


class MyApp(App):
    def build(self):
        return MyW()


if __name__ == "__main__":
    MyApp().run()
