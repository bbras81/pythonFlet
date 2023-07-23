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
            ft.Text("Internet", font_family="Rooster", style="displayLarge", color="#ff3300"),
            ft.Text("Speed", font_family="Rooster", style="displayLarge", color="#ffff00")
        ], 
        alignment="center"
    )
    
    # defining terminal lines for printing the text
    line_01 = ft.Text(value="Press start...", font_family="SourceCode", color="#ffffff")
    line_02 = ft.Text(value="", font_family="SourceCode", color="#1aff1a")
    line_03 = ft.Text(value="", font_family="SourceCode", color="#1aff1a")
    progressBar = ft.ProgressBar(width=400, color="#0080ff", bgcolor="#eeeeee", opacity=0)
    progress_text = ft.Text("  ", font_family="SourceCode" opacity=0)
    progress_row = ft.Row([progressBar, progress_text])
    line_04 = ft.Text(value="", font_family="SourceCodeBold", color="#ffff00")
    line_05 = ft.Text(value="", font_family="SourceCode", color="#1aff1a")
    progressBar = ft.ProgressBar(width=400, color="#0080ff", bgcolor="#eeeeee", opacity=0)
    progress_text = ft.Text("  ", font_family="SourceCode" opacity=0)
    progress_row = ft.Row([progressBar, progress_text])
    line_06 = ft.Text(value="", font_family="SourceCode", color="#1aff1a")
    line_07 = ft.Text(value="", font_family="SourceCodeBold", color="#ffff00")
    line_08 = ft.Text(value="", font_family="SourceCode", color="#ffffff")
    progressBar = ft.ProgressBar(width=400, color="#0080ff", bgcolor="#eeeeee", opacity=0)
    progress_text = ft.Text("  ", font_family="SourceCode" opacity=0)
    progress_row = ft.Row([progressBar, progress_text])
    terminal_text = ft.Column([line_01, line_02, line_03, line_04, line_05, line_06, line_07, line_08])
    
    # terminal container
    
    getSpeedContainer = ft.Container(
        content=terminal_text
        width=200,
        height=100,
        bgcolor="#4d4d4d",
        border_radius=30,
        padding=20,
        animate=ft.animation.Animation(1000, "bounceOut")
    )
    def animate_getSpeedContainer(e):
        getSpeedContainer.width = 700
        getSpeedContainer.height = 400
        getSpeedContainer.update()
    
    #page components
    page.add(
        appTitle,
        getSpeedContainer,
        ft.IconButton(icon=ft.icons.PLAY_CIRCLE_FILL_OUTLINED,on_click=animate_getSpeedContainer,icon_color="#1aff1a", icon_size = 50)
    )



#executing the main function
ft.app(target=main, assets_dir="assets")