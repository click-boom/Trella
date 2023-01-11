import tkinter as tk
from PIL import ImageTk, Image
from tkinter import ttk

login=tk.Tk()
def loginpage():
    
    #--------------------Login Window-------------------------------------------------------------
    
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
    login_frame=tk.Frame(login, width='700', height='700')
    login_frame.place(x=620, y=220)


    #--------------------"Welcome To TRELLA"-------------------------------------------------------------
    login.txt='Welcome To Trella'
    login.heading=tk.Label(login, 
     text=login.txt,
     font=('yu gothic ui', '28', 'bold'),
     fg='#6c6c6c').place(x=780, y=450, width=400, height=50)


    #--------------------"Logo"-------------------------------------------------------------
    logo_img=tk.PhotoImage(file=('/home/wae/Documents/giri raj sir/Trella/llogo.png'))    
    login.logo_lbl=tk.Label(login_frame,image=logo_img)
    login.logo_lbl.image=logo_img
    login.logo_lbl.place(x=285, y=30)
    
loginpage() 
login.mainloop() 