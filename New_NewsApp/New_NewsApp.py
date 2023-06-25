from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, CardTransition, FadeTransition
from kivy.uix.floatlayout import FloatLayout

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.

# Define a string variable to store the kv code
kv = """
<MyW>:
    # Use a FloatLayout as the root widget
    FloatLayout:
        # Add an ActionBar widget as a child of the FloatLayout
        ActionBar:
            pos_hint: {'top': 1}
            ActionView:
                use_separator: True
                
                ActionPrevious:
                    title: 'News'
                    with_previous: False
                
                ActionButton:
                    text: 'Btn0'
                    icon: 'floppy.png'
                
                ActionButton:
                    text: 'Btn1'
                
                ActionButton:
                    text: 'Btn2'
                
                ActionButton:
                    text: 'Btn3'
                
                ActionButton:
                    text: 'Btn4'
                
                ActionGroup:
                    text: 'Group'
           
                    ActionButton:
                        text: 'Btn5'
           
                    ActionButton:
                        text: 'Btn6'
           
                    ActionButton:
                        text: 'Btn7'

<MyW1>:
    # Use a FloatLayout as the root widget
    FloatLayout:
        # Add two Button widgets as children of the FloatLayout
        Button:
            id: label1
            size_hint: .2, .2
            pos_hint: {'center_x': .5, 'center_y': .5}
            text: 'B1'
        
        Button:
            id: label2
            size_hint: .1, .1
            pos_hint: {'center_x': .1, 'center_y': .1}
            text: 'B2'
            
"""

# Load the kv code using Builder.load_string()
Builder.load_string(kv)

# Define a class for the first screen that inherits from FloatLayout
class MyW(FloatLayout):
    def __init__(self, **kwargs):
        super(MyW, self).__init__(**kwargs)
        self.add_widget(MyW1())
        

# Define a class for the second screen that inherits from FloatLayout
class MyW1(FloatLayout):
    pass

# Define a class for the app that inherits from App
class New_NewsApp(App):
    def build(self):
        return MyW()


if __name__ == "__main__":
    New_NewsApp().run()
