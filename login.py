import tkinter as tk
from PIL import ImageTk, Image
from tkinter import ttk

login=tk.Tk()
def loginpage():
    
    #--------------------Login WIndow-------------------------------------------------------------
    
    login.title('Welcome to Trella')
    login.geometry('800x600')
    login.maxsize(1920,1080)
    login.resizable()

    #--------------------Page Background-------------------------------------------------------------
    img=ImageTk.PhotoImage(Image.open('/home/wae/Documents/giri raj sir/Trella/bg.png'))
    bg=tk.Label(login, image=img)
    bg.image=img
    bg.pack(fill='both', expand='yes')


    #--------------------Login Frame-------------------------------------------------------------
    login_frame=tk.Frame(login, bg='#d6d6d6', width='700', height='500')
    login_frame.place(x=620, y=400)


    #--------------------"Welcome To TRELLA"-------------------------------------------------------------
    login.txt='Welcome To Trella'
    login.heading=tk.Label(login, 
     text=login.txt,
     font=('yu gothic ui', '25', 'bold'),
     fg='#6c6c6c').place(x=810, y=400, width=300, height=50)



    #--------------------"Logo"-------------------------------------------------------------
    llogo=tk.PhotoImage(file='/home/wae/Documents/giri raj sir/Trella/llogo.png')
    logo=tk.Label(login, image=llogo).place(x=10, y=10)


loginpage()
login.mainloop()