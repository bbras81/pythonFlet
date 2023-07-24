import flet as ft

'''
Theory:

1) UserControl should cll self.update() to push its hanges to the flet page.


2) super().__init__() must be always called in your constructor
'''


class Counter(ft.UserControl):
    def __init__(self, initial_count):
        super().__init__()
        self.counter = initial_count
        
    def add_click(self, e):
        self.counter +=1
        self.text.value = str(self.counter)
        self.update()
    
    def build(self):
        self.text = ft.Text(str(self.counter))
        self.add_button = ft.ElevatedButton("+", on_click=self.add_click)
        return ft.Row([self.text, self.add_button])
    
    
def main(page: ft.Page):
    page.add(Counter(100))


ft.app(target=main)