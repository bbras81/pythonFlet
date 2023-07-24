import flet as ft
import time, threading

'''
Theory: Usercontrol provide life.cycle hook nethods

1) did_mount() : Called aftter UserControl added to the page 
2) will_mount() : called before the UserControl is removed from the page
'''
'''
Theory: Deamon

1) In multi-tasking computer os, a deamon is a computer program thart runs a background process, rather than being under the direct control of an interactive user.
'''
class MyTimer(ft.UserControl):
    def __init__(self, seconds):
        super().__init__()
        self.seconds = seconds
        
    def did_mount(self):
        self.running == True
        self.myThread = threading.Thread(target=self.update_timer, args=(), deamon = True)
        self.myThread.start()
        
    def will_unmount(self):
        self.running = False
        
    def update_timer(self):
        while self.seconds and self.running:
            mins, secs = divmod(self.seconds, 60)
            self.countdown.value ="{:02d}:{:02d}".format(mins, secs)
            self.update()
            time.sleep(1)
            self.seconds -= 1 
            
    def build(self):
        self.countdown = ft.Text()
        return self.countdown

def main(page: ft.Page):
    page.add(MyTimer(120))



ft.app(target=main)