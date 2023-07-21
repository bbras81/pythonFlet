# Importing the library
import flet as ft


#Definig the main funtion
def main(page: ft.Page):
    
    #Setting the page title 
    page.Title = "Single Greeting app!"
    
    #Taking ferst name / last name
    first_name = ft.TextField(label="First Name", autofocus=True )
    last_name = ft.TextField(label="Last Name")
    
    #Column for greetings the user
    greetings = ft.Column()
    
    
    
    def btn_click(e):
        greetings.controls.append(ft.Text(f"Hello {first_name.value} {last_name.value}"))
        first_name.value=""
        last_name.value=""
        first_name.focus()
        page.update()
    
    
    #button
    hello = ft.ElevatedButton("Say Hello", on_click=btn_click)
    
    page.add(
        first_name,
        last_name,
        hello,
        greetings
    )
    
ft.app(target=main)