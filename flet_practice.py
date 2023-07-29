import flet as ft
import time
import os


def main(page: ft.Page):
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

    output_text = ft.Ref[ft.Text]()
    submit_button = ft.Ref[ft.ElevatedButton]()
    color_dropdown = ft.Ref[ft.Dropdown]()
    my_row = ft.Ref[ft.Row]()
    
    def button_clicked1(e):
        output_text.current.value = f"Dropdown value is: {color_dropdown.current.value}"
        page.update()
        
    # page.controls.append(ft.Row(ref=my_row,controls= [
    #     ft.Dropdown(label="Color", options=["Red", "Green", "Blue"], ref=color_dropdown),
    #     ft.ElevatedButton(text="Submit", on_click=button_clicked1, ref=submit_button),
    #     ft.Text(value="",ref=output_text)
    # ]))
    
    page.controls.append(ft.Row(ref=my_row,controls= [
        ft.Dropdown(width = 100, options=[
            ft.dropdown.Option("Red"),
            ft.dropdown.Option("Green"),
            ft.dropdown.Option("Blue"),], ref=color_dropdown),
        ft.ElevatedButton(text="Submit", on_click=button_clicked1, ref=submit_button),
        ft.Text(value="", ref=output_text, bgcolor = f'{color_dropdown.current.value}', width = 300),
    ]))
   
    
    def grid_items(r: ft.Row):
        for i in range(10):
            r.controls.append(
                ft.Container(
                    ft.Text(f" الله أكبر {i+1}"),
                        width=100,
                        height=100,
                        alignment=ft.alignment.center,
                        bgcolor=ft.colors.RED,
                        border=ft.border.all(1, ft.colors.AMBER_400),
                        border_radius=ft.border_radius.all(5),
                
            )
                
        )
        return r.controls
    
    my_grid_view = ft.Row()
    page.controls.append(ft.Row(ref=my_grid_view,controls= grid_items(my_grid_view), wrap=True,scroll="always", expand= 10, width=1000))
    
    
    page.clean() 

    my_image = ft.Image(src= "/home/mood/Documents/NewsApp/MyMeditationApp/i.jpg",fit="contain", width=100, height=100)
    page.add(my_image)

    page.title = "Drag and Drop example"

    def drag_accept(e):
        # get draggable (source) control by its ID
        src = page.get_control(e.src_id)
        # update text inside draggable control
        src.content.content.value = "0"
        # update text inside drag target control
        e.control.content.content.value = "1"
        page.update()

    page.add(
        ft.Row(
            [
                ft.Draggable(
                    group="number",
                    content=ft.Container(
                        width=50,
                        height=50,
                        bgcolor=ft.colors.CYAN_200,
                        border_radius=5,
                        content=ft.Text("1", size=20),
                        alignment=ft.alignment.center,
                    ),
                ),
                ft.Container(width=100),
                ft.DragTarget(
                    group="number",
                    content=ft.Container(
                        width=50,
                        height=50,
                        bgcolor=ft.colors.PINK_200,
                        border_radius=5,
                        content=ft.Text("0", size=20),
                        alignment=ft.alignment.center,
                    ),
                    on_accept=drag_accept,
                ),
            ]
        )
    ) 

    page.clean()
    
    page.add(ft.Text(f"Initial route: {page.route}"))
    
    def route_change1(e: ft.RouteChangeEvent):
        page.add(ft.Text(f"Route changed to: {e.route}"))
    
    def go_store(e):
        page.route = "/store"
        page.update()
        
    page.on_route_change = route_change1
    page.add(ft.ElevatedButton("Go to Store", on_click=go_store))
    
  
    
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

ft.app(target=main, view=ft.AppView.WEB_BROWSER)