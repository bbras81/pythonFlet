#import libraries
import flet as ft
import speedtest
from time import sleep

#define a main function
def main(page: ft.Page):
    
    page.title = "Internet Speed Test"
    page.theme_mode = "dark"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.window_bgcolor = "blue"
    page.padding = 30
    page.bgcolor = "#000000"
    
    #enable scroll in the page
    page.auto_scroll = True 
    
    # configuring the fonts
    page.fonts = {
        "Rooster" : "fonts/RoosterPersonalUse-3z8d8.ttf",
        "SourceCode" : "fonts/SourceCodePro-BlackItalic.ttf",
        "SourceCodeBold" : "fonts/SourceCodePro-Bold.ttf"
    }
    
    # make the heading of the app
    appTitle = ft.Row(
        controls = [
            ft.Text("INTERNET", font_family="Rooster", style="displayLarge", color="#ff3300"),
            ft.Text("SPEED", font_family="Rooster", style="displayLarge", color="#ffff00")
        ]
    )
    
    
    #page components
    page.add(
        appTitle,
        #getSpeedContainer,
        ft.IconButton(icon=ft.icons.PLAY_CIRCLE_FILL_OUTLINED)
    )



#executing the main function
ft.app(target=main, assets_dir="assets")