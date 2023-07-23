import flet as ft

def main(page: ft.Page):
    page.title = "Guess Me"
    #Configuring the fonts
    
    page.fonts = {
        "SpaceMission" : "fonts/SpaceMission-rgyw9.otf"
    }
    
    
    page.add(
        ft.Row(
            controls=[
                ft.Text(value="GUESS ME", font_family="SpaceMission", size=26)
            ], alignment="center"
        )
    )

ft.app(target=main, assets_dir="assets")