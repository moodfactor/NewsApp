from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import MDList
from kivymd.uix import scrollview


kv = '''
MDBoxLayout:
    orientation: "vertical"
        
    ScrollView:
        MDBoxLayout:
            orientation: "vertical"
            padding: "24dp"
            spacing: "24dp"
            adaptive_height: True

    MDBoxLayout:
        adaptive_height: True
        padding: "8dp"
        spacing: "8dp"
            
        MDRaisedButton:
            text: 'Get Online data'
            on_release: 
                
        MDRaisedButton:
            text: 'Clear data'
            on_release: 
'''


class MainApp(MDApp):
    def build(self):
        return Builder.load_string(kv)


if __name__ == "__main__":
    MainApp().run()
