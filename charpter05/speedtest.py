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
    
    st = speedtest.Speedtest()


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
    progressBar_01 = ft.ProgressBar(width=400, color="#0080ff", bgcolor="#eeeeee", opacity=0)
    progress_text_01 = ft.Text(" ", font_family="SourceCodePro-BlackItalic", opacity=0)
    progress_row_01 = ft.Row([progressBar_01, progress_text_01])
    line_04 = ft.Text(value="", font_family="SourceCodeBold", color="#ffff00")
    line_05 = ft.Text(value="", font_family="SourceCode", color="#1aff1a")
    progressBar_02 = ft.ProgressBar(width=400, color="#0080ff", bgcolor="#eeeeee", opacity=0) 
    progress_text_02 = ft.Text(" ", font_family="SourceCodePro-BlackItalic", opacity=0)
    progress_row_02 = ft.Row([progressBar_02, progress_text_02])
    line_06 = ft.Text(value="", font_family="SourceCode", color="#1aff1a")
    line_07 = ft.Text(value="", font_family="SourceCodeBold", color="#ffff00")
    line_08 = ft.Text(value="", font_family="SourceCode", color="#ffffff")
    progressBar_03 = ft.ProgressBar(width=400, color="#0080ff", bgcolor="#eeeeee", opacity=0)
    progress_text_03 = ft.Text(" ", font_family="SourceCodePro-BlackItalic", opacity=0)
    progress_row_03 = ft.Row([progressBar_03, progress_text_03])
    terminal_text = ft.Column([line_01, line_02, line_03, line_04, line_05, line_06, line_07, line_08])
    
  # terminal container
    getSpeedContainer = ft.Container(
        content = terminal_text,
        width=200,
        height=100,
        bgcolor="#4d4d4d",
        border_radius=30,
        padding=20,
        animate=ft.animation.Animation(1000, "bounceOut"),
    )
    
    def animate_getSpeedContainer(e):
        getSpeedContainer.update()
        
        getSpeedContainer.width = 700
        getSpeedContainer.height = 400
        line_01.value = "> calculating download speed, please wait."
        getSpeedContainer.update()
        sleep(1)
        
        ideal_server = st.get_best_server() #This will find out and connecto to the best server possible
        city = ideal_server["name"]
        country = ideal_server["country"]
        cc = ideal_server["cc"]
        line_02.value = f"> finding the best possible server in {city}, {country} ({cc})"
        getSpeedContainer.update()
        sleep(2)
        
        line_03.value = "> connections establisched, status ok, fetching the download speed."
        progress_row_01.opacity = 1
        progressBar_01.opacity = 1
        download_speed = st.download()/1024/1024 # bytes per second to Mbps
        progressBar_01.value = 1
        line_04.value = f"> the download speed is {str(round(download_speed, 2))} Mbps."
        getSpeedContainer.update()
        line_05.value = "> calculating upload speed, please wait"
        sleep(1)
        
        line_06.value = "> executing upload script, hold on"
        progress_row_02.opacity = 1
        progressBar_02.opacity = 1
        getSpeedContainer.update()
        upload_speed = st.upload()/1024 / 1024 #bytes to Mbps
        progressBar_02.value = 1
        line_07.value = f"> the upload speed is {str(round(upload_speed, 2))}"
        getSpeedContainer.update()
        sleep(1)
        line_08.value = "> task completed successfully \n\n >> app developer: kumar anurag (instagram: kmrang)" 
        getSpeedContainer.update()
        
        
        
        
        

    #page components
    page.add(
        appTitle,
        getSpeedContainer,
        ft.IconButton(icon=ft.icons.PLAY_CIRCLE_FILL_OUTLINED,on_click=animate_getSpeedContainer,icon_color="#1aff1a", icon_size = 50)
    )



#executing the main function
ft.app(target=main, assets_dir="assets")