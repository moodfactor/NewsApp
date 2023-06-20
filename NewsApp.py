from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ObjectProperty


class NewsHome(BoxLayout):
    
    label_text  = StringProperty("Hi")
    label_1 = ObjectProperty()

    def change_label(self, value) -> str:
       self.ids.my_button.text = value
       
       return value

    
class NewsApp(App):
    def build(self):
        return NewsHome()


if __name__ == '__main__':
    NewsApp().run()
