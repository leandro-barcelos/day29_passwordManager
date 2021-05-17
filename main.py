from tkinter import *


root = Tk()

class Application:
    def __init__(self) -> None:
        self.root = root
        self.passwords = []
        self.screen()
        self.password_frame()
        root.mainloop()
        
    def screen(self):
        self.root.title("Password Manager")
        self.root.configure(bg="#2d2d34")
        icon = PhotoImage(file="src/icon.png")
        self.root.iconphoto(False, icon)
        self.root.geometry("1200x800")
        self.root.resizable(False, False)

    def password_frame(self):
        start_x = 25
        for i in range(4):
            frame = Frame(self.root, bg="#e2dcde") 
            frame.place(relx=start_x, rely=10, relheight=80, relwidth=1150)
            self.passwords.append(frame)
            start_x += 90
            
        

Application()