import flet as ft

def main(page: ft.Page):

    page.Title = 'Calculator'
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"

    display = ft.TextField()

    def add_number(e):
        number = e.data
        print(number)



    page.add(
        ft.Row(
            controls=[
                display
            ],
            alignment="center"
        ),
        ft.Row(
            controls=[
                ft.ElevatedButton(text="1", on_click=add_number, data="1"),
                ft.ElevatedButton(text="2", on_click=add_number, data="2"),
                ft.ElevatedButton(text="3", on_click=add_number, data="3")
            ],
            alignment="center"
        ),
        ft.Row(
            controls=[
                ft.ElevatedButton(text="4"),
                ft.ElevatedButton(text="5"),
                ft.ElevatedButton(text="6")
            ],
            alignment="center"
        ),
        ft.Row(
            controls=[
                ft.ElevatedButton(text="7"),
                ft.ElevatedButton(text="8"),
                ft.ElevatedButton(text="9")
            ],
            alignment="center"
        ),
        ft.Row(
            controls=[
                ft.ElevatedButton(text="*"),
                ft.ElevatedButton(text="0"),
                ft.ElevatedButton(text="#")
            ],
            alignment="center"
        )
    )


ft.app(target=main)
