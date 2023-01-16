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


    #--------------------Functions---------------------------------------------------------------
    

    th_clr='#d6d6d6'
    fnt='#6c6c6c'
    btn_bg='#a4a4a4'


    #--------------------Page Background-------------------------------------------------------------


    img=ImageTk.PhotoImage(Image.open('/home/wae/Documents/giri raj sir/Trella/Images/bg.png'))
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
     font=('yu gothic ui', '30', 'bold'),
     fg='#6c6c6c').place(x=780, y=435, width=400, height=50)


    #-----------------------------------"Logo"-------------------------------------------------------------


    logo_img=tk.PhotoImage(file=('/home/wae/Documents/giri raj sir/Trella/Images/dlogo.png'))    
    login.logo_lbl=tk.Label(login_frame,image=logo_img)
    login.logo_lbl.image=logo_img
    login.logo_lbl.place(x=288, y=25)


    #------------------------------"Sign in and Password"---------------------------------------------------


    login.usrname_lbl=tk.Label(login_frame, text='Username', fg=fnt, font=('yu gothic ui', 18, 'bold'))
    login.usrname_lbl.place(x=120, y=300)
    login.usrname_entry=tk.Entry(login_frame, highlightthickness=0, relief='flat', fg=fnt, bg=th_clr, font=('yu gothic ui', 15, 'bold'))
    login.usrname_entry.place(x=120, y=340, width=450)

    login.username_line=tk.Canvas(login_frame, width=400, height=2.0, bg=fnt, highlightthickness=0)
    login.username_line.place(x=120, y=370, width=450)

    login.passwd_lbl=tk.Label(login_frame, text='Password', fg='#6c6c6c', font=('yu gothic ui', 18, 'bold'))
    login.passwd_lbl.place(x=120, y=410)
    login.passwd_entry=tk.Entry(login_frame, highlightthickness=0, relief='flat', fg=fnt, bg=th_clr,show="*",font=('yu gothic ui', 15, 'bold'))
    login.passwd_entry.place(x=120, y=450, width=450)

    login.passwd_line=tk.Canvas(login_frame, width=450, height=2.0, bg=fnt, highlightthickness=0)
    login.passwd_line.place(x=120, y=478)


    #--------------------"Sign in and Password icons"-------------------------------------------------------
   
   
    username_img=tk.PhotoImage(file=('/home/wae/Documents/giri raj sir/Trella/Images/userr-icon.png'))    
    login.user_logo_lbl=tk.Label(login_frame,image=username_img)
    login.user_logo_lbl.image=username_img
    login.user_logo_lbl.place(x=88, y=342)


    passwd_img=tk.PhotoImage(file=('/home/wae/Documents/giri raj sir/Trella/Images/pwd_icon.png'))    
    login.passwd_logo_lbl=tk.Label(login_frame,image=passwd_img)
    login.passwd_logo_lbl.image=passwd_img
    login.passwd_logo_lbl.place(x=88, y=450)


    #--------------------"Login Button"-------------------------------------------------------


    btn_img=tk.PhotoImage(file=('/home/wae/Documents/giri raj sir/Trella/Images/btn.png'))    
    login.login_btn_img=tk.Label(login_frame,image=btn_img)
    login.login_btn_img.image=btn_img
    login.login_btn_img.place(x=225, y=510)

    login_btn=tk.Button(login.login_btn_img, text='Sign in', font=('yu gothic ui', 18, 'bold'),width=10, bd=0, highlightthickness=0,  bg=btn_bg, cursor='hand2', activebackground=btn_bg, fg='white' )
    login_btn.place(x=30, y=8)


    #--------------------"Signup Button"-------------------------------------------------------


    login.sign_up_label=tk.Button(login_frame, text='Not registered yet? Sign Up', font=('yu gothic ui', 18, 'bold underline'),background=th_clr, foreground=fnt, activebackground=th_clr,cursor='hand2', bd=0, width=20)
    login.sign_up_label.place(x=185, y=570)


    #--------------------"Hide/Unhide Option"----------------------------------------------------------

    
    def show():
        login.hide_pwd_btn=tk.Button(login_frame, image=login.hide_pwd_img, bg=th_clr, activebackground=th_clr, cursor='hand2', bd=0, command=hide)
        login.hide_pwd_btn.image=login.hide_pwd_img
        login.hide_pwd_btn.place(x=537, y=448)
        login.passwd_entry.config(show='')

    def hide():
        login.view_pwd_btn=tk.Button(login_frame, image=login.view_pwd_img, bg=th_clr, activebackground=th_clr, cursor='hand2', bd=0, command=show)
        login.hide_pwd_btn.image=login.hide_pwd_img
        login.hide_pwd_btn.place(x=537, y=448)
        login.passwd_entry.config(show='*')
    

    login.view_pwd_img=ImageTk.PhotoImage(Image.open('/home/wae/Documents/giri raj sir/Trella/Images/view_pwd.png'))    
    login.view_pwd_btn=tk.Button(login_frame, image=login.view_pwd_img, bg=th_clr, activebackground=th_clr, cursor='hand2', bd=0, command=show)
    login.view_pwd_btn.image=login.view_pwd_img
    login.view_pwd_btn.place(x=537, y=448)

    login.hide_pwd_img=ImageTk.PhotoImage(Image.open('/home/wae/Documents/giri raj sir/Trella/Images/hide_pwd.png'))    


loginpage()
login.mainloop() 