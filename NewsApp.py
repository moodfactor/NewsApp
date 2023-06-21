from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ObjectProperty
from kivy.clock import Clock
from kivy.uix import widget
from kivy.uix import button, label


class NewsHome():

    label_text = StringProperty("Hi")
    label_1 = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
       

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
