import time
import playsound
def start_timer():
    duration = float(input("Enter duration in minutes: "))
    start_time = time.time()
    end_time = start_time + duration * 60
    while time.time() < end_time:
        time.sleep(1)
    playsound.playsound("sound.wav")
    print("Timer finished!")

start_timer()