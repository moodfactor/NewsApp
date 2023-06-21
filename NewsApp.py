from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ObjectProperty
from kivy.clock import Clock
from kivy.uix import widget


class NewsHome(BoxLayout):
    
    label_text  = StringProperty("Hi")
    label_1 = ObjectProperty()

    def change_label(self, value) -> str:
       self.ids.my_button.text = value
       
       return value
   
    def my_callback(self, dt):
        self.ids.label_test.text = "My callback is called! " + str(dt)
        
    def on_touch_down(self, touch):
        Clock.schedule_once(self.my_callback, 1)
        return super().on_touch_down(touch)

    
class NewsApp(App):
    def build(self):
        return NewsHome()


if __name__ == '__main__':
    NewsApp().run()
