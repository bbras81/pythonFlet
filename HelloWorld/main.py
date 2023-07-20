import flet as ft 

def main(page: ft.Page):
    #Defenindo o titulo da página
    page.title = "Hello, World"

    
    #flet text control
    text = ft.Text(value="My first Flet App!")

    
    #juntando e atualizando em relação à pagina
    page.controls.append(text)
    page.update()

ft.app(target=main)