import flet as ft

def main(page: ft.Page):
    
    page.add(
        #Para escrever elementos numa linha
        ft.Row(controls=[ft.Text("My Favorite Fruits: \n")]),
        ft.Row(
            controls=[
                ft.Text("Apple"),
                ft.Text("Mango"),
                ft.Text("Guava")
            ] 
        ),
        #Para escrever elementos numa coluna 
    ft.Column(controls=[ft.Text("My Favorite Cricketer \n")]),
    ft.Column(
        controls=[
            ft.Text("Akjcnksvdjn"),
            ft.Text("sdfsvwrew"),
            ft.Text("Tono")
        ]
        )
    ),
    
    
    
ft.app(target=main) 