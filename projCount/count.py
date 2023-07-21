import flet as ft

def main(page: ft.Page):
    page.title = "Calculator"
    page.scroll= "adaptive"   

 
    
    width = ft.TextField(value="" , text_align=ft.TextAlign.RIGHT, width=100)
    height = ft.TextField(value="", text_align=ft.TextAlign.RIGHT, width=100)
    
    resWidth = ft.TextField(value="", text_align=ft.TextAlign.RIGHT, width=100)
    resHeight = ft.TextField(value="", text_align=ft.TextAlign.RIGHT, width=100)
    
    result = ft.TextField(value="", text_align=ft.TextAlign.RIGHT, width=100)

    
    def calculate(width, height, resWidth, resHeight):
        if len.resWidth == 0:
            result.value = 'olaola'
            page.update()
        elif len.resHeight == 0:
            result = str(int(height) * int(resWidth) / int(width))
            page.update()
        return result

    
    page.add(
        ft.Row(
            [
                ft.Text("Enter Width:", size=22),
                width,
            ], 
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [
                ft.Text("Enter Height:", size=22),
                height,
                
            ], 
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [
                ft.Text("New Width", size=22),
                resWidth,
            ], 
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [
                ft.Text("New Height", size=22),
                resHeight,
            ], 
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [
                ft.ElevatedButton(text="Clear"),
                ft.ElevatedButton(text="Calculate", on_click=calculate),

            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [
                ft.Text("Result", size=22),
                result,
            ], 
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

ft.app(target=main)