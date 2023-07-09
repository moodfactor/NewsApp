from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.recycleview import RecycleView
from kivymd.uix.card import MDCard
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.properties import StringProperty

KV = '''
<CustomCard>:
    orientation: "vertical"
    background_color: 1, 1, .2, .8
    
    MDCard:
        size_hint: None, None
        size: 300, 200
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        elevation: 4
        radius: [20,]
        md_bg_color: 1, 1, 1, 1
        on_press: print("Press")
            
        BoxLayout:
            orientation: "vertical"
            spacing: 10
            padding: 10
            
            Image:
                source: "image.jpeg"
                size_hint: 1, 1
                pos_hint: {"center_x": 0.5, "center_y": 0.5}
                allow_stretch: True
            
            MDLabel:
                text: "Ahmed"
                size_hint: 1, 0.2
                halign: "center"
                color: (0, 0, 0, 1)
                font_style: "H6"
                pos_hint: {"center_x": 0.5, "center_y": 0.5}

RecycleView:
    viewclass: 'CustomCard'
    data: app.data
    RecycleBoxLayout:
        elevation: 4
        default_size: None, dp(200)
        default_size_hint: 1, None
        size_hint_y: None
        height: self.minimum_height
        orientation: "vertical"
'''

class CustomCard(RecycleDataViewBehavior, MDCard):
    text = StringProperty()

class MyApp(MDApp):
    data = [{'text': f"Item {i}"} for i in range(20)]

    def build(self):
        return Builder.load_string(KV)

MyApp().run()