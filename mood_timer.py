# Import kivymd and kivy modules
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
import playsound

def play_sound():
    playsound.playsound('sound.wav')

# Define the app layout in kv language
kv = '''
BoxLayout:
    orientation: 'vertical'
    MDTopAppBar:
        title: 'Timer App'
    BoxLayout:
        orientation: 'horizontal'
        padding: 20
        spacing: 20
        MDTextField:
            id: input
            hint_text: 'Enter time in minutes'
            input_filter: 'int'
            max_text_length: 2
            halign: 'center'
            size_hint_x: 0.2
        MDIconButton:
            icon: 'play-circle-outline'
            on_release: app.start_timer()
    MDLabel:
        id: timer
        text: '00:00'
        halign: 'center'
        font_style: 'H2'
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
        self.sound = None # The sound to play when the timer is done

    # Start the timer when the button is pressed
    def start_timer(self):
        # Get the input from the text field and convert it to an integer
        try:
            self.time = int(self.root.ids.input.text) * 60
        except ValueError:
            return # Do nothing if the input is not valid

        # Reset the timer label to show the input time
        self.minutes = self.time // 60
        self.seconds = self.time % 60
        self.root.ids.timer.text = f'{self.minutes:02}:{self.seconds:02}'

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
            self.sound = play_sound()
           

# Run the app
TimerApp().run()
