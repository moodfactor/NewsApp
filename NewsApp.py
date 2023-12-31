from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty, ObjectProperty
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.uix.switch import Switch
from kivy.properties import BooleanProperty
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label

letters = ["txt 1", "txt 2", "txt 3", "txt 5", "txt 6"]

class MButton(Button):
    pass

class NewsHome(BoxLayout, Widget):

    label_text = StringProperty("Hi")
    label_1 = ObjectProperty()
    
    # create a property that will be updated when the switch is active or not
    switch_state = BooleanProperty(False)
    

    def __init__(self, **kwargs):
        super(NewsHome, self).__init__(**kwargs)
        
        for l in letters:
            s = Screen(name= l)
            s.add_widget(Label(text=l))
            self.ids.sm.add_widget(s)
            self.ids.buttons.add_widget(MButton(text=l))

        '''
            To create an event dispatcher buttons
 with custom events,
            you need to register the name of the event
            in the class and then create a method of the same name.
            The method will be called when the event is dispatched.
        '''
        self.register_event_type('on_test')

    class MButton(Button):
        pass

        
    def textinput_callback(self, value):
        self.ids.textinput_label_mirror.text = str(value)
        
    def on_switch_state(self, *args):
        # update the label text when the switch is active or not
        # Beware "Switch is OFF" if self.ids.switch.active else "Switch is ON"
        if self.ids.switch.active:
            self.ids.switch_label_state.text = "Switch is OFF"
        else:
            self.ids.switch_label_state.text = "Switch is ON"
    
    # custom event fn.
    def on_test(self, *args):
        self.ids.label_test2.text = ">>>>>>>>>>>>>>"

    # dispatch event to {on_test}.
    def do_something(self):
        # when do_something is called, the 'on_test' event will be
        # dispatched with the value
        self.dispatch('on_test')
        
    
        
    def on_swipe(self, value):
        if self.ids.swipe_button.text == "Click Me":
            self.ids.swipe_button.text = "Swipe Me"
        else:
            self.ids.swipe_button.text = "Click Me"

    def on_press_button(self):
        self.dispatch('on_swipe', 'on_swipe')
        
   

    def state_callback(self, obj, value):        
        print("State changed for ", obj, "to ", value)
        super().state_callback(obj, value)

    def on_press_callback(self) -> str:
        #in .kv Beware to call the function with ()  (ex: on_press_callback())
        self.ids.label_test2.text = "press on button"
        print("Booooooom")

    def change_label(self, value) -> str:
        self.ids.my_button.text = value

        return value

    def my_callback(self, dt):
        self.ids.label_test.text = "My callback is called! " + str(dt)

    def on_touch_down(self, touch):
        Clock.schedule_interval(self.my_callback, 1/30)
        if touch.is_double_tap:
            self.ids.label_test.text = ''
            Clock.unschedule(self.my_callback)
        return super().on_touch_down(touch)


class NewsApp(App):
    def build(self):
        return NewsHome()


if __name__ == '__main__':
    NewsApp().run()
