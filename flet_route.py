import flet as ft
import time


def main (page: ft.page):
    
     t1 = ft.Text(value="Hello World!", color= "green")
     page.controls.append(t1)
     t = ft.Text()
     page.add(t)
     for i in range(10):
        t.value = f'Step {i}'
        t.update()
        time.sleep(.1)
        
     page.add(
        ft.Row(controls=[
        ft.Text("A"),
        ft.Text("B"),
        ft.Text("C")
        ])
    )

     page.add(
        ft.Row(controls=[
            ft.TextField(label="Your name"),
            ft.ElevatedButton(text="Say my name!")
        ])
    )
     page.update()
    
     def button_clicked(e):
        for i in range(10):
            nonlocal t
            t = ft.Text()
            page.add(t)
            t.value = f'Step {i}'
            t.update()
            time.sleep(.1)
    
     page.add(ft.ElevatedButton(text="Click me!", on_click=button_clicked))

     def add_clicked(e):
        page.add(ft.Checkbox(label = new_task.value, visible= True))
        new_task.value = ""
        new_task.focus()
        new_task.update()
        page.update()
    
     new_task = ft.TextField(hint_text= "Whats needs to be done?", width= 300)
     page.add(ft.Row([new_task, ft.ElevatedButton("Add", on_click=add_clicked)]))
    
     page.title = "Routes Example"

     def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.AppBar(title=ft.Text("Flet app"), bgcolor=ft.colors.SURFACE_VARIANT),
                    ft.ElevatedButton("Visit Store", on_click=lambda _: page.go("/store")),
                ],
            )
        )
        if page.route == "/store":
            page.views.append(
                ft.View(
                    "/store",
                    [
                        ft.AppBar(title=ft.Text("Store"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                    ],
                )
            )
        page.update()

     def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

     page.on_route_change = route_change
     page.on_view_pop = view_pop
     page.go(page.route)

    
     page.scroll = "always"
     page.update()

ft.app(target=main, )