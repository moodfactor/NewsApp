import flet as ft

def main(page: ft.page):
    
    list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    dropdown = ft.Dropdown()

    def mm(anyList):
        for i in anyList:
            dropdown.options.append(ft.dropdown.Option(str(i)))
        return dropdown.options
            
    page.update()
        
        
       
    dropdown.options = mm(list)    
    page.add(dropdown)
    page.update()
    
ft.app(target=main)