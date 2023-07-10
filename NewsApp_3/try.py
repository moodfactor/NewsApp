from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.recycleview import RecycleView
from kivymd.uix.card import MDCard
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.properties import StringProperty

KV = '''


<CustomCard>:
    BoxLayout:
        size_hint: None, None
        size: 300, 200
        pos_hint: {"center_x": 0.4, "center_y": 0.5}
        elevation: 4
        radius: [20,]
        md_bg_color: .3, .3, 1, 1
        orientation: "vertical"
    
        canvas.before:
            Color:
                rgba: .8, .5, .1,  # canvas white color
            
            
            Rectangle:
                pos: self.pos
                size: 200, 300
                
    
        MDCard:
            size_hint: None, None
            size: 300, 200
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            elevation: 4
            radius: [20,]
            md_bg_color: 0, 1, 1, 1 # aqua color
            on_press: print("Press")
            
            
            BoxLayout:
                orientation: "vertical"
                

            
                Image:
                    source: "image.jpeg"
                    size_hint: 1, 1
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}
                    allow_stretch: True
            
                MDLabel:
                    text: "Ahmed"
                    size_hint: 1, 0.2
                    halign: "center"
                    color: (0, 1, 0, 1)
                    font_style: "H6"
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}

RecycleView:
    viewclass: 'CustomCard'
    data: app.data
    size_hint: 1, 1
    
    RecycleBoxLayout:
        elevation: 2
        spacing: 10
        padding: 10
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