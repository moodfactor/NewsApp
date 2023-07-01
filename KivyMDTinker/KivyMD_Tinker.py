from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.toast import toast
from kivymd.app import MDApp

KV = '''
MDScreen:
    MDTopAppBar:
        title: 'Test Toast'
        pos_hint: {'bottom': 1}
        left_action_items: [['menu', lambda x: x]]
    MDRaisedButton:
        text: 'TEST KIVY TOAST'
        pos_hint: {'center_x': .5, 'center_y': .5}
        on_release: app.show_toast()
    '''
    
class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_string(KV)
    
    def show_toast(self):
        toast("Hello World",background = [0.2, 0.5, 1, 1], duration=2.0)
MainApp().run()