import kivy
from kivy.app import App
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.card import MDCard
from kivy.lang import Builder
from kivymd.uix.button import MDIconButton
from kivy.properties import StringProperty
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.factory import Factory
from kivy.properties import BooleanProperty



KV = """
<Main>:
    Boxlayout:
        orientation: "vertical"
        

        CustomCard:
            Boxlayout:
                orientation: "vertical"   
    
                MDCard:
                    size_hint: None, None
                    size: 300, 200
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}
                    elevation: 2
                    radius: [20,]
                    md_bg_color: 1, 1, 1, 1
                    on_press: print("Press")
            
                    BoxLayout:
                        orientation: "vertical"
                        spacing: 10
                        padding: 10
            
                        Image:
                            source: ""
                            size_hint: 1, 1
                            pos_hint: {"center_x": 0.5, "center_y": 0.5}
                            allow_stretch: True
            
                        MDLabel:
                            text: ""
                            size_hint: 1, 0.2
                            halign: "center"
                            color: (0, 0, 0, 1)
                            font_style: "H6"
                            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            
            
                    MDIconButton:
            
                        icon: "share-variant"
                        pos_hint: {"right": 0.95, "top": 0.95}

        RecycleView:
            id: rv
            layout: layout
            viewclass: "CustomCard"
            data: app.data
            RecycleBoxLayout:
                
        
"""

Builder.load_string(KV)

class CustomCard(RecycleDataViewBehavior, MDCard, FocusBehavior, LayoutSelectionBehavior, BoxLayout):
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)
    image_source = StringProperty()
    text = StringProperty()
    def __init__(self, **kwargs):
        super(CustomCard, self).__init__(**kwargs)
        self.index = None
        self.selected = False
        self.selectable = True
        self.image_source = ""
        self.text = ""
        
    def refresh_view_attrs(self, rv, index, data):
        self.index = index
        self.image_source = data["image_source"]
        self.text = data["text"]
        return super(CustomCard, self).refresh_view_attrs(rv, index, data)
    
    def apply_selection(self, rv, index, is_selected):
        print(f"selection changed to {is_selected} at {index}")
        self.selected = is_selected
        if is_selected:
            print("selected")
        else:
            print("unselected")
    
    
    def refresh_view_attrs(self, rv, index, data):
        self.index = index
        return super(CustomCard, self).refresh_view_attrs(rv, index, data)
    
    def on_touch_down(self, touch):
        if super(CustomCard, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos):
            return self.parent.select_with_touch(self.index, touch)
    
    def apply_selection(self, rv, index, is_selected):
        print(f"selection changed to {is_selected} at {index}")
        self.selected = is_selected
        if is_selected:
            print("selected")
        else:
            print("unselected")
    
class RecycleViewApp(App):
    def __init__(self, **kwargs):
        super(RecycleViewApp, self).__init__(**kwargs)
        self.data = [{
            "image_source": "https://images.unsplash.com/photo-1534983821759-8b9e3d8d8f7b?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60",
            "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nonne merninisti licere mihi ista probare, quae sunt a te dicta? Refert tamen, quo modo."
        },
        ]
        for i in range(100):
            self.data.append({
                "image_source": "https://images.unsplash.com/photo-1534983821759-8b9e3d8d8f7b"},
                                {"text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nonne merninisti licere mihi ista probare, quae sunt a te dicta? Refert tamen, quo modo."})
            
                    
            
            
class Main(BoxLayout):
    pass

class NewsApp(MDApp):
    def build(self):
        return Main()
        
    
if __name__ == "__main__":
     NewsApp().run()
