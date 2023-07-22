import flet as ft

def main(page: ft.Page):
    page.title="Counter"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    number_sum = ft.TextField(value="0", width=150, text_align=ft.TextAlign.CENTER)
    number_sub = ft.TextField(value="100", width=150, text_align=ft.TextAlign.CENTER)
    
    def sum_fnc(e):
        number_sum.value = str(int(number_sum.value)+5)
        page.update()
        
    def sub_fnc(e):
        number_sub.value = str(int(number_sub.value)-5)
        page.update()
    
    # NÃO ME POSSO ESQUECER DO PAGE.ADD
    page.add(
        ft.Row(
            controls=[
                ft.IconButton(ft.icons.HOUSE, on_click=sum_fnc),
                number_sum,
                number_sub,
                ft.IconButton(ft.icons.HOUSE, on_click=sub_fnc)
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )
    
    
    
ft.app(target=main)