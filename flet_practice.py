import flet as ft
import time



def main(page: ft.Page):
    t = ft.Text(value="Hello World!", color= "green")
    page.controls.append(t)
    t = ft.Text()
    page.add(t)
    for i in range(10):
        t.value = f'Step {i}'
        t.update()
        time.sleep(1)
        
    page.update()

ft.app(target=main)