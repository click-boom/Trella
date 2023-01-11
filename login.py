import tkinter as tk
from PIL import ImageTk, Image
from tkinter import ttk





login=tk.Tk()
def loginpage():
    
    #--------------------Login Window-------------------------------------------------------------
    
    # screen_width = win.winfo_screenwidth()
    # screen_height = win.winfo_screenheight()
    
    login.title('Welcome to Trella')
    login.geometry('1920x1080')
    login.minsize(1920,1080)

    th_clr='#d6d6d6'
    fnt='#6c6c6c'
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
     fg='#6c6c6c').place(x=780, y=435, width=400, height=50)


    #-----------------------------------"Logo"-------------------------------------------------------------
    logo_img=tk.PhotoImage(file=('/home/wae/Documents/giri raj sir/Trella/llogo.png'))    
    login.logo_lbl=tk.Label(login_frame,image=logo_img)
    login.logo_lbl.image=logo_img
    login.logo_lbl.place(x=288, y=25)


    #------------------------------"Sign in and Password"---------------------------------------------------


    login.username_lbl=tk.Label(login_frame, text='Username', fg=fnt, font=('yu gothic ui', 16, 'bold'))
    login.username_lbl.place(x=90, y=300)
    login.username_entry=tk.Entry(login_frame, highlightthickness=0, relief='flat', fg=fnt, bg=th_clr, font=('yu gothic ui', 12, 'bold'))
    login.username_entry.place(x=88, y=335, width=270)

    login.username_line=tk.Canvas(login_frame, width=300, height=2.0, bg=fnt, highlightthickness=0)
    login.username_line.place(x=88, y=360)

    login.passwd_lbl=tk.Label(login_frame, text='Password', fg='#6c6c6c', font=('yu gothic ui', 16, 'bold'))
    login.passwd_lbl.place(x=90, y=400)
    login.passwd_entry=tk.Entry(login_frame, highlightthickness=0, relief='flat', fg=fnt, bg=th_clr, font=('yu gothic ui', 12, 'bold'))
    login.passwd_entry.place(x=88, y=432, width=270)

    login.password_line=tk.Canvas(login_frame, width=300, height=2.0, bg=fnt, highlightthickness=0)
    login.password_line.place(x=88, y=458)

    #--------------------"Sign in and Password icons"-------------------------------------------------------
   
   
    username_img=tk.PhotoImage(file=('/home/wae/Documents/giri raj sir/Trella/userr-icon.png'))    
    login.user_logo_lbl=tk.Label(login_frame,image=username_img)
    login.user_logo_lbl.image=username_img
    login.user_logo_lbl.place(x=53, y=339)


    passwd_img=tk.PhotoImage(file=('/home/wae/Documents/giri raj sir/Trella/pwd_icon.png'))    
    login.passwd_logo_lbl=tk.Label(login_frame,image=passwd_img)
    login.passwd_logo_lbl.image=passwd_img
    login.passwd_logo_lbl.place(x=53, y=435)


    #--------------------"Password Eye Button"-------------------------------------------------------
    
    
    
    #--------------------"Login Button"-------------------------------------------------------
    # login.login_btn=ImageTk.PhotoImage(Image.open(''))
loginpage()
login.mainloop() 