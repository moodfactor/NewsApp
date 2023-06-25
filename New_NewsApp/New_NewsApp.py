from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, CardTransition, FadeTransition
from kivy.uix.floatlayout import FloatLayout

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
Builder.load_string("""
<MyW>:
    Button: 
        id: label1
        size_hint: .5, .5
        pos_hint: {'center_x': .5, 'center_y': .5}
        text: 'B2'
    
    Button:
        id: label2
        size_hint: .1, .1
        pos_hint: {'center_x': .1, 'center_y': .1}  
        text: 'B1'
    
    Button:
        id: label1
        size_hint: .1, .1
        pos_hint: {'center_x': .9, 'center_y': .9}  
        text: 'B3'
        
        """)

class MyW(FloatLayout):
    pass



class New_NewsApp(App):
    def build(self):
        return MyW()


if __name__ == "__main__":
    New_NewsApp().run()