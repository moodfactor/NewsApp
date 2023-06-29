from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import MDList
from kivymd.uix import scrollview
from kivymd_extensions.akivymd.uix.loaders import AKLabelLoader, AKImageLoader
from kivy.network.urlrequest import UrlRequest
from threading import Thread
import requests

kv = '''
MDBoxLayout:
    orientation: "vertical"
        
    ScrollView:
        MDBoxLayout:
            orientation: "vertical"
            padding: "24dp"
            spacing: "24dp"
            adaptive_height: True
            
            LoaderCard:
                id: user1
            
            LoaderCard:
                id: user2

    MDBoxLayout:
        adaptive_height: True
        padding: "8dp"
        spacing: "8dp"
            
        MDRaisedButton:
            text: 'Get Online data'
            on_release: app.get_data()
                
        MDRaisedButton:
            text: 'Clear data'
            on_release: app.clear_data() 
            
<LoaderCard@MDCard>:
    padding: "8dp"
    size_hint: None, None
    size: "200dp", "200dp"
    pos_hint: {"center_x": .5, "center_y": .5}
    elevation: 2
    name: ''
    email: ''
    website: ''
    avatar: ''
    
    MDBoxLayout:

        MDFloatLayout:
            size_hint_x: 0.3
            
            AKImageLoader:
                size_hint: None, None
                size: "50dp", "50dp"
                pos_hint: {"center_x": .5, "center_y": .5}
                source: root.avatar
        
        MDBoxLayout:
            orientation: "vertical"
            size_hint_x: 0.7
            padding: "8dp"
            spacing: "8dp"
            
            #name
            DataLoaderLabel:
                text: root.name
                
            MDSeparator:
            
            #Email
            DataLoaderLabel:
                text: root.email
            
            #Website
            DataLoaderLabel:
                text: root.website
                
            MDSeparator:
            
                

<DataLoaderLabel@AKLabelLoader>:
    size_hint_y: None
    height: "24dp"
    theme_text_color: "Primary"
    halign: "left"
    
        
'''


class MainApp(MDApp):
    def build(self):
        return Builder.load_string(kv)

    def get_data(self, *args):
        print("get data ...")
        t = Thread(target=self.request_data)
        t.start()
        t.join()
        print("get data done")

    # set the first user
    def set_user1(self, *args):
        user1 = args[1]
        self.root.ids.user1.avatar = self.users['user1']['avatar']
        self.root.ids.user1.name = self.users['user1']['name']
        self.root.ids.user1.email = self.users['user1']['email']
        self.root.ids.user1.website = self.users['user1']['website']
    
    def set_user2(self, *args):
        user2 = args[1]
        self.root.ids.user2.avatar = self.users['user2']['avatar']
        self.root.ids.user2.name = self.users['user2']['name']
        self.root.ids.user2.email = self.users['user2']['email']
        self.root.ids.user2.website = self.users['user2']['website']
    
    def get(self):
        """
        Sends the request to the server and returns the response object.
        """
        response = requests.get(self.url)
        return response
    
    # request data from the web according to the user
    def request_data(self, *args):
        url = 'https://gist.githubusercontent.com/moodfactor/89a903b8e791e481a2aa452e6b6357cd/raw/d5cf09e9653f5893ab837193461e3141abbc68ff/users' 
        
        response = UrlRequest(url).result
        
        if response.ok:
            self.set_user1(response.result)
            self.set_user2(response.result)
        else:
            print("Error: {} {}".format(response.status_code, response.error))
        
        return True
    
   
        
    def get_error(self, *args):
        print("error")
        
    def clear_data(self, *args):
        self.root.ids.user1.avatar = ''
        self.root.ids.user1.name = ''
        self.root.ids.user1.email = ''
        self.root.ids.user1.website = ''
        
        self.root.ids.user2.avatar = ''
        self.root.ids.user2.name = ''
        self.root.ids.user2.email = ''
        self.root.ids.user2.website = ''
        
    # make the json file for def set_user1
    def make_json(self, *args):
       # self.make_json_file = json.dumps(self.users)
        '''
        make the json file for def set_user1
        
        
        '''
        
        self.users = {
            'user1': {
                'name': 'John Doe',
                'email': 'XXXXXXXXXXXX',
            }, 
            'user2': {
                      'name': 'John Doe',
                      'email': 'XXXXXXXXXXXX',
                      'website': 'http://www.john.com',
                      'avatar': 'https://randomuser.me/api/portraits/men/1.jpg'
                      
            
        }
        }
        
        

if __name__ == "__main__":
    MainApp().run()
