import flet as ft
from random import randint

def main(page: ft.Page):
    page.title = "Guess Me"
    page.padding = 30
    
    #Configuring the fonts
    
    answer = randint(1, 100)
    print("=>", answer)
    
    
    page.fonts = {
        "SpaceMission" : "fonts/SpaceMission-rgyw9.otf",
        "uncracked" : "fonts/Uncracked-X3WjK.otf"
    }
    
    
    
    player_1 = ft.TextField(hint_text="Guess a number (1-100)...", label="Player 1", border_radius=20)
    player_2 = ft.TextField(hint_text="Guess a number (1-100)...", label="Player 2", border_radius=20)
    result = ft.Text(font_family="uncracked", size=45)
    
    #Printing the result
    
    def check_guess_player_1(e):
        if int(player_1.value) < answer:
            result.value = "Guess a heiger value"
        elif int(player_1.value) > answer:
            result.value = "Guess a smaller value"
        elif int(player_1.value) == answer:
            result.value = "Congratulations! Player 1 won the game!"
        else:
            result.value = "Something went wrong"
        page.update()
            
    
    def check_guess_player_2(e):
        if int(player_2.value) < answer:
            result.value = "Guess a heiger value"
        elif int(player_2.value) > answer:
            result.value = "Guess a smaller value"
        elif int(player_2.value) == answer:
            result.value = "Congratulations! Player 2 won the game!"
        else:
            result.value = "Something went wrong"
        page.update()
        
    
    #Checker buttons
    check_player_1 = ft.ElevatedButton("Check your gess", on_click=check_guess_player_1)
    check_player_2 = ft.ElevatedButton("Check your gess", on_click=check_guess_player_2)
    
    
    
    page.add(
        ft.Card(
            ft.Container(
                content = ft.Row(
                    controls=[ft.Text(value="GUESS ME", font_family="SpaceMission", size=26)],
                    alignment="center"
                ),
                padding=20   
            ),
        ),
        ft.Column(
            controls = [
            ft.Row([player_1, check_player_1]),
            ft.Row([player_2, check_player_2]),
            result,
           ], 
            horizontal_alignment="center"
        ),
    )
    
    
ft.app(target=main, assets_dir="assets")
