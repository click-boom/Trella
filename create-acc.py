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
    login.resizable(1, 1)


    #--------------------Functions---------------------------------------------------------------
    
    th_clr='#d6d6d6'
    fnt='#6c6c6c'

    #--------------------Page Background-------------------------------------------------------------
    img=ImageTk.PhotoImage(Image.open('/home/wae/Documents/giri raj sir/Trella/bg.png'))
    bg=tk.Label(login, image=img)
    bg.image=img
    bg.pack(fill='both', expand='yes')


    #--------------------Login Frame-------------------------------------------------------------
    login_frame=tk.Frame(login, width='700', height='720',background=th_clr)   
    login_frame.place(x=620, y=220)


    #--------------------"Welcome To TRELLA and Sign Up label"-------------------------------------------------------------
    login.txt='Welcome To Trella'
    login.heading=tk.Label(login, 
     text=login.txt,
     font=('yu gothic ui', '30', 'bold'),
     fg='#6c6c6c',background=th_clr).place(x=780, y=420, width=400, height=50)

    login.txt='Sign Up'
    login.heading=tk.Label(login, 
     text=login.txt,
     font=('yu gothic ui', '18', 'bold'),
     fg='#6c6c6c',background=th_clr).place(x=780, y=475, width=400, height=50)


    #-----------------------------------"Logo"-------------------------------------------------------------
    logo_img=tk.PhotoImage(file=('/home/wae/Documents/giri raj sir/Trella/dlogo.png'))    
    login.logo_lbl=tk.Label(login_frame,image=logo_img,background=th_clr)
    login.logo_lbl.image=logo_img
    login.logo_lbl.place(x=288, y=15)


    #------------------------------"Sign Up and Password"---------------------------------------------------


    login.username_lbl=tk.Label(login_frame, text='Username', fg=fnt,background=th_clr, font=('yu gothic ui', 16, 'bold'))
    login.username_lbl.place(x=120, y=300)
    login.username_entry=tk.Entry(login_frame, highlightthickness=0, relief='flat', fg=fnt, bg=th_clr, font=('yu gothic ui', 13, 'bold'))
    login.username_entry.place(x=120, y=330, width=450)

    login.username_line=tk.Canvas(login_frame, width=400, height=2.0, bg=fnt, highlightthickness=0)
    login.username_line.place(x=120, y=358, width=450)

    login.email_lbl=tk.Label(login_frame, text='Email', fg='#6c6c6c',background=th_clr, font=('yu gothic ui', 16, 'bold'))
    login.email_lbl.place(x=120, y=375)
    login.email_entry=tk.Entry(login_frame, highlightthickness=0, relief='flat', fg=fnt, bg=th_clr,font=('yu gothic ui', 13, 'bold'))
    login.email_entry.place(x=120, y=412, width=450)

    login.email_line=tk.Canvas(login_frame, width=450, height=2.0, bg=fnt, highlightthickness=0)
    login.email_line.place(x=120, y=440)

    login.passwd_line=tk.Canvas(login_frame, width=450, height=2.0, bg=fnt, highlightthickness=0)
    login.passwd_line.place(x=120, y=590)

    login.epasswd_lbl=tk.Label(login_frame, text='Enter Password', fg='#6c6c6c', bg=th_clr, font=('yu gothic ui', 16, 'bold'))
    login.epasswd_lbl.place(x=120, y=452)
    login.epasswd_entry=tk.Entry(login_frame, highlightthickness=0, relief='flat', fg=fnt, bg=th_clr,show="*",font=('yu gothic ui', 13, 'bold'))
    login.epasswd_entry.place(x=120, y=488, width=450)

    login.epasswd_line=tk.Canvas(login_frame, width=450, height=2.0, bg=fnt, highlightthickness=0)
    login.epasswd_line.place(x=120, y=517)
    
    login.cpasswd_lbl=tk.Label(login_frame, text='Confirm Password', fg='#6c6c6c', bg=th_clr, font=('yu gothic ui', 16, 'bold'))
    login.cpasswd_lbl.place(x=120, y=530)
    login.cpasswd_entry=tk.Entry(login_frame, highlightthickness=0, relief='flat', fg=fnt, bg=th_clr,show="*",font=('yu gothic ui', 13, 'bold'))
    login.cpasswd_entry.place(x=120, y=565, width=450)


    login.password_line=tk.Canvas(login_frame, width=450, height=2.0, bg=fnt, highlightthickness=0)
    login.password_line.place(x=120, y=595)

    

    #--------------------"Sign in and Password icons"-------------------------------------------------------
   
   
    username_img=tk.PhotoImage(file='/home/wae/Documents/giri raj sir/Trella/userr-icon.png')    
    login.user_logo_lbl=tk.Label(login_frame,bg=th_clr ,image=username_img)
    login.user_logo_lbl.image=username_img
    login.user_logo_lbl.place(x=85, y=327)

    # email_img=tk.PhotoImage(file=('D:/trela/email_icon.png'))    
    # login.email_logo_lbl=tk.Label(login_frame,bg=th_clr ,image=email_img)
    # login.email_logo_lbl.image=email_img
    # login.email_logo_lbl.place(x=85, y=410)

    passwd_img=tk.PhotoImage(file=('/home/wae/Documents/giri raj sir/Trella/pwd_icon.png'))    
    login.passwd_logo_lbl=tk.Label(login_frame,bg=th_clr ,image=passwd_img)
    login.passwd_logo_lbl.image=passwd_img
    login.passwd_logo_lbl.place(x=85, y=490)

    passwd_img=tk.PhotoImage(file=('/home/wae/Documents/giri raj sir/Trella/pwd_icon.png'))    
    login.passwd_logo_lbl=tk.Label(login_frame,bg=th_clr ,image=passwd_img)
    login.passwd_logo_lbl.image=passwd_img
    login.passwd_logo_lbl.place(x=85, y=568)


    #--------------------"Password Eye Button"-------------------------------------------------------




    
    
    
    
    #--------------------"Sign Up Button"-------------------------------------------------------
    # btn_img=tk.PhotoImage(file=('D:/trela/btn.png'))    
    # login.btn_img=tk.Label(login_frame,image=btn_img)
    # login.btn_img.image=btn_img
    # login.btn_img.place(x=190, y=510)

    # login_btn=tk.Button(login.login_btn_img, text='Sign in', font=('yu gothic ui', 18, 'bold'),width=10, bd=0, highlightthickness=0,  bg=btn_bg, cursor='hand2', activebackground=btn_bg, fg=fnt )
    # login_btn.place(x=60, y=8)
loginpage()
login.mainloop() 