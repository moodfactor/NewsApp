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
        for i in range(500):
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
    page.controls.append(ft.Row(ref=my_grid_view,controls= grid_items(my_grid_view), wrap=True, scroll="always", expand= True))
    
    page.scroll = "always"
    page.update()

ft.app(target=main)