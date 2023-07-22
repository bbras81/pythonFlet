import flet as ft

def main(page: ft.Page):

    page.title = "Counter app"

    txt_number = ft.TextField(value="0", width=100, text_align="center")
    page.theme_mode = "light"
    page.vertical_alignment = "center"

    page.add(
        ft.Row(
            controls=[
                ft.IconButton(ft.icons.REMOVE),
                txt_number,
                ft.IconButton(ft.icons.ADD)
            ],
            alignment="center"
        )
    )

ft.app(target=main)
