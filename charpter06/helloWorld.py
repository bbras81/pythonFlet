import flet as ft

'''
Theory: Why do we need User Controls


1) UserControl allows building isolated re-usable components by combining the existing Flet Controls.

2) UserControl must implement builb() that is called to bild the control's UI.

3) Build() should return a single control instance or a listo of controls.


'''

class GreetingsControl(ft.UserControl):
    def build(self):
        text = ft.Text("Hello World.")
        return ft.Row([text, ft.ElevatedButton("hi")])
    


def main(page: ft.Page):

    page.add(GreetingsControl(), GreetingsControl())
    
    


ft.app(target=main)
