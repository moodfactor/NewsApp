import flet as ft
import requests
import asyncio

def main(page: ft.page):
    
    # A list of available times for booking an appointment with a tutor
    times = ["10:00 AM", "11:00 AM", "12:00 PM", "1:00 PM", "2:00 PM", "3:00 PM", "4:00 PM"]
    
    page.title = "Tutor Booking dates"
    
    # A function that makes a post request to httpbin.org with the date
    # async def book_appointment(date):
    #     # The url for the post request
    #     url = "https://httpbin.org/post"
    #     # The data to be sent as json
    #     data = {"date": date}
    #     # Make the post request and get the response
    #     response = requests.post(url, json=data)
    #     # Log the data and print it to terminal for debug
    #     print(f"Booked appointment for {date}")
    #     print(response.json())
    
    dropdown = ft.Dropdown()
    def ff(times_list):
        for n in times_list:
            dropdown.options.append(ft.dropdown.Option(str(n)))
        return dropdown.options
            
        
    
    
    def update_label(e):
        label.value = str(dropdown.value)
        label.update()
    
    label = ft.Text()
    
    dropdown.options = ff(times)
    dropdown.on_change = update_label
    
    
    label2= ft.Text("Select a time: ")
    page.add(ft.Column(controls=[label2,dropdown, label],spacing= 16, horizontal_alignment=ft.CrossAxisAlignment))
    page.update()
    
ft.app(target=main)