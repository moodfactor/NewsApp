# Import kivymd and kivy modules
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from kivymd.uix.menu import MDDropdownMenu
from kivy.core.window import Window

# Define the app layout in kv language
kv = '''
BoxLayout:
    orientation: 'vertical'
    MDTopAppBar:
        title: 'Timer App'
        md_bg_color: app.theme_cls.primary_color
        elevation: 10
    BoxLayout:
        orientation: 'horizontal'
        padding: 20
        spacing: 20
        MDDropDownItem:
            id: drop_item
            text: 'Select time in minutes'
            pos_hint: {'center_y': 0.5}
            font_style: 'H6'
            current_item_color: app.theme_cls.primary_color
        MDIconButton:
            id: play_button
            icon: 'play-circle-outline'
            on_release: app.start_timer()
            pos_hint: {'center_y': 0.5}
            user_font_size: '64sp'
    MDLabel:
        id: timer
        text: '00:00'
        halign: 'center'
        font_style: 'H1'
'''

# Define the app class
class TimerApp(MDApp):
    # Initialize the app
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.root = Builder.load_string(kv)
        self.time = 0 # The total time in seconds
        self.minutes = 0 # The minutes part of the time
        self.seconds = 0 # The seconds part of the time
        self.event = None # The clock event for updating the timer
        self.sound = SoundLoader.load('alarm.wav') # The sound to play when the timer is done

        # Create a list of menu items from 1 to 30 minutes
        menu_items = [{"text": f"{i}"} for i in range(1, 31)]

        # Create a menu object with the menu items and an on_select function
        self.menu = MDDropdownMenu(
            caller=self.root.ids.play_button,
            items=menu_items,
            width_mult=4,
            on_select=self.set_time,
            pos=self.root.ids.play_button.pos,
        )

        # Bind a callback function to the mouse_pos property of the window
        Window.bind(mouse_pos=self.on_mouse_pos)

    # Set the time from the menu item selected by the user
    def set_time(self, instance):
        
        # Get the text of the menu item and convert it to an integer
        try:
            self.time = int(instance.text) * 60
        except (ValueError, KeyError):
            self.time = 0

        # Update the drop down item text to show the selected time
        self.root.ids.drop_item.set_item(instance.text)

        # Reset the timer label to show the input time
        self.minutes = self.time // 60
        self.seconds = self.time % 60

    # Start the timer when the button is pressed
    def start_timer(self):
        
        # Cancel any previous clock event if exists
        if self.event:
            self.event.cancel()

        # Schedule a new clock event to update the timer every second
        self.event = Clock.schedule_interval(self.update_timer, 1)

    # Update the timer every second
    def update_timer(self, dt):
        # Decrease the time by one second
        self.time -= 1

        # Update the minutes and seconds parts of the time
        self.minutes = self.time // 60
        self.seconds = self.time % 60

        # Update the timer label to show the remaining time
        self.root.ids.timer.text = f'{self.minutes:02}:{self.seconds:02}'


        # If the time reaches zero, stop the clock event and play the sound
        if self.time == 0:
            self.event.cancel()
            if self.sound:
                self.sound.play()

    # Callback function for the mouse_pos property
    def on_mouse_pos(self, window, pos):
        # Get the play button instance
        play_button = self.root.ids.play_button

        # Check if the mouse is over the play button
        if play_button.collide_point(*pos):
            # Open the menu
            self.menu.open()
        else:
            # Dismiss the menu
            self.menu.dismiss()

# Run the app
TimerApp().run()
