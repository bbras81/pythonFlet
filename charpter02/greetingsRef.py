# Importing the library
import flet as ft


#Definig the main funtion
def main(page: ft.Page):
    
    #Setting the page title 
    page.Title = "Single Greeting app with reference!"
    
    #Taking ferst name / last name
    first_name = ft.Ref[ft.TextField]()
    last_name = ft.Ref[ft.TextField]()
    
    #Column for greetings the user
    greetings = ft.Ref[ft.Column]()
    
    
    
    def btn_click(e):
        greetings.current.controls.append(ft.Text(f"Hello {first_name.current.value} {last_name.current.value}"))
        first_name.current.value=""
        last_name.current.value=""
        first_name.current.focus()
        page.update()
    
    
    page.add(
        ft.TextField(ref=first_name,label="First Name", autofocus=True),
        ft.TextField(ref=last_name, label="Last Name"),
        ft.ElevatedButton("Say hello!", on_click=btn_click),
        ft.Column(ref=greetings)
    )
    
ft.app(target=main)
 
'''
NOTE:
1) All the flex control have a property know as ref
'''