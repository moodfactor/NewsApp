from kivy import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


kv = """

<MyW>:
    canvas:
    
        Ellipse:
            pos: 0, 0
            size: 50, 50
            on_touch_down: root.on_press(print("Ellipse"))
            
            
        Rectangle:
            pos: 500, 0
            size: 50, 50
            
        Triangle:
            points: 100, 0, 200, 300, 0, 300
            segments: 
            
        Line: 
            points: 300, 0, -350, 500
"""

Builder.load_string(kv)


class MyW(Button):
    pass


class MyApp(App):
    def build(self):
        return MyW()


if __name__ == "__main__":
    MyApp().run()
