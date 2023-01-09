import tkinter as tk
from PIL import ImageTk, Image
from tkinter import ttk

login=tk.Tk()
def loginpage():
    login.title('Welcome to Trella')
    login.geometry('800x600')
    login.maxsize(1920,1080)
    login.resizable()

    img=ImageTk.PhotoImage(Image.open('/home/wae/Documents/giri raj sir/Trella/1.png'))
    bg=tk.Label(login, image=img)
    bg.image=img
    bg.pack(fill='both', expand='yes')

    # login_frame=tk.Frame(login, bg='#d6d6d6', width)
    

loginpage()
login.mainloop()