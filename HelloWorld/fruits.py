import flet as ft

def main(page: ft.Page):
    
    page.add(
        ft.Row(controls=[ft.Text("My Favorite Fruits: \n")])
    )
    
    
    ft.app(target=main) 