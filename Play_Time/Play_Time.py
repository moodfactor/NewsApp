from kivy import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Ellipse, Line, Rectangle, Triangle
from kivy.graphics.transformation import Matrix
from kivy.uix.scatter import Scatter
from kivy.animation import Animation


kv = """

<MyW>:
    # sky blue color
    background_color: 0, 0, 1, 1 
    on_touch_down: print("on_touch_down")
    
     
    canvas:
        Color: 
        # Fuchia color
            rgb: 1, 0, 1
  
    Button:
        id: button_1
        text: "Button 1"
        on_press: root.animate(button_1)    
               
        Ellipse:
            pos: 0, 0
            size: 50, 50
            on_touch_down: root.on_press(print("Ellipse"))
            
            
        Rectangle:
            pos: 500, 0
            size: 50, 800
            
        Rectangle:
            pos: 0, 500
            size: 800, 50    
            
        Triangle:
            points: 400, 200, 300, 400, 400, 400
            
        Line: 
            points: 300, 300, 600, 600
    
    Button: 
        id: my_button
        text: 'Hello world'
        size_hint: None, None

        pos_hint: {'center_x': .5, 'center_y': .5}
        canvas.before:
            PushMatrix
            Rotate:
                angle: 45
                origin: self.center
            Translate:
                xy: self.center_x, self.center_y
        canvas.after:
            PopMatrix
"""

Builder.load_string(kv)


class MyW(Button):
    def __init__(self, **kwargs):
        super(MyW, self).__init__(**kwargs)
        # with self.canvas:
        #     self.ellipse = Ellipse(pos=self.pos, size=(10, 10))

        # self.bind(pos=self.update_ellipse)
        # self.bind(size=self.update_ellipse)

        # but1 = Button(text="Button 1")
        # scatter = Scatter(size=(400, 400), size_hint=(None, None))

        # scatter.add_widget(but1)
        # self.add_widget(scatter)

    def animate(self, instance):
        animation = Animation(pos=(100, 100), t='out_bounce', duration=2)
        animation += Animation(pos=(200, 100), t='out_bounce', duration=2)
        animation &= Animation(pos=(500, 500), t='out_bounce', duration=2)
        animation += Animation(size=(100, 50))
        animation.start(instance)

    def rotate_button(button, angle):
        matrix = Matrix()
        matrix.rotate(angle)
        button.canvas.before.add(matrix)

    def update_ellipse(self, *args):
        self.ellipse.pos = self.pos
        self.ellipse.size = self.size


class MyApp(App):
    def build(self):
        return MyW()


if __name__ == "__main__":
    MyApp().run()
