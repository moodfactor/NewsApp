from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import WipeTransition, Screen, CardTransition, FadeTransition
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.

# Define a string variable to store the kv code
kv = """
<MyW>:
    BoxLayout: 
    # set the size_hint_y to -1 so that the height is set automatically
    # based on the content, and now it takes the whole window
        
        size_hint_y: -1
        height: 30
        id: buttons
    
    # Create a screen manager to switch between screens
    ScreenManager:
    # Give an id to the screen manager for easy reference
        id: sm
 
        

<MButton>:
    on_press: app.root.ids.sm.current = self.text
        
            
"""


# Load the kv code using Builder.load_string()
Builder.load_string(kv)

# Define a class for the first screen that inherits from FloatLayout


class MyW(BoxLayout):
    def __init__(self, **kwargs):
        super(MyW, self).__init__(**kwargs)

        # Create a screen with the name "Hello1"
        s = Screen(name="Hello1")
        # Add a label with the text "src1" to the screen
        s.add_widget(Label(text="src1"))
        # Add the screen to the screen manager
        self.ids.sm.add_widget(s)
        # Set the transition type for the screen manager to WipeTransition
        self.ids.sm.transition = FadeTransition()

        # Create another screen with the name "Hello2"
        s = Screen(name="Hello2")
        # Add a label with the text "src2" to the screen
        s.add_widget(Label(text="src2"))
        # Add the screen to the screen manager
        self.ids.sm.add_widget(s)
        # Set the transition type for the screen manager to WipeTransition
        self.ids.sm.transition = WipeTransition()

        # Create a button with the text "Hello1"
        self.ids.buttons.add_widget(MButton(
            text="Hello1"))
        # Create another button with the text "Hello2"
        self.ids.buttons.add_widget(MButton(
            text="Hello2"))


# Define a class for the second screen that inherits from FloatLayout
class MButton(Button):
    pass

# Define a class for the app that inherits from App


class New_NewsApp(App):
    def build(self):
        return MyW()


if __name__ == "__main__":
    New_NewsApp().run()
