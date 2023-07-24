import flet as ft

def main(page: ft.Page):
    #setting the page title
    page.title = "To-Do App"
    
    #Taking input from user
    input_text = ft.TextField(hint_text="What do you want to do today...", width=350)
    
    def button_click(e):
        page.add(ft.Checkbox(label=input_text.value))
     
    #aligning the input text and the botton on the row
    page.add(
        ft.Row(
            [
                input_text,
                ft.ElevatedButton(text="Add", on_click=button_click)
            ]
        )   
    )
ft.app(target=main)