from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, CardTransition, FadeTransition
from kivy.uix.floatlayout import FloatLayout

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
Builder.load_string("""
<MyW>:
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
        
        """)

class MyW(FloatLayout):
    pass



class New_NewsApp(App):
    def build(self):
        return MyW()


if __name__ == "__main__":
    New_NewsApp().run()