import tkinter as tk
from PIL import ImageTk, Image
login=tk.Tk()

import sqlite3
conn=sqlite3.connect('reg_usrs.db')
c=conn.cursor()

def login_backend():

    ue=usrname_entry.get()
    
    passwd=passwd_entry.get()

    c.execute("SELECT username FROM users")
    usernames = c.fetchall()
    

    c.execute("SELECT email FROM users")
    umails = c.fetchall()


    if((ue ,) in usernames) or ((ue ,) in umails):
        c.execute("SELECT * FROM users WHERE email")
        uname=c.fetchall()
        print(uname)
        c.execute("SELECT * FROM users WHERE username=ue")
        umail=c.fetchall()
        print(umail)
    else:
        return
def login_frontend():
    
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

    def signup_link():
        login.destroy()
        import signup



    #--------------------Page Background-------------------------------------------------------------


    img=ImageTk.PhotoImage(Image.open('D:/Trella/Images/bg.png'))
    bg=tk.Label(login, image=img)
    bg.image=img
    bg.pack(fill='both', expand='yes')



    #--------------------Login Frame-------------------------------------------------------------


    login_frame=tk.Frame(login, width='700', height='700',bg=th_clr)
    login_frame.place(x=620, y=220)

    #--------------------"Welcome To TRELLA"-------------------------------------------------------------


    login.txt='Welcome To Trella'
    heading=tk.Label(login, 
     text=login.txt,
     font=('yu gothic ui', '30', 'bold'),
     fg='#6c6c6c')
    heading.place(x=780, y=435, width=400, height=50)


    #-----------------------------------"Logo"-------------------------------------------------------------


    logo_img=tk.PhotoImage(file=('D:/trela/Images/dlogo.png'))    
    logo_lbl=tk.Label(login_frame,image=logo_img,bg=th_clr)
    logo_lbl.image=logo_img
    logo_lbl.place(x=288, y=25)


    #------------------------------"Sign in and Password"---------------------------------------------------


    usrname_lbl=tk.Label(login_frame, text='Username', fg=fnt, font=('yu gothic ui', 18, 'bold'))
    usrname_lbl.place(x=120, y=300)
    global usrname_entry
    usrname_entry=tk.Entry(login_frame, highlightthickness=0, relief='flat', fg=fnt, bg=th_clr, font=('yu gothic ui', 15, 'bold'))
    usrname_entry.place(x=120, y=340, width=450)

    username_line=tk.Canvas(login_frame, width=400, height=2.0, bg=fnt, highlightthickness=0)
    username_line.place(x=120, y=370, width=450)

    passwd_lbl=tk.Label(login_frame, text='Password', fg='#6c6c6c', font=('yu gothic ui', 18, 'bold'))
    passwd_lbl.place(x=120, y=410)
    global passwd_entry
    passwd_entry=tk.Entry(login_frame, highlightthickness=0, relief='flat', fg=fnt, bg=th_clr,show="*",font=('yu gothic ui', 15, 'bold'))
    passwd_entry.place(x=120, y=450, width=450)

    passwd_line=tk.Canvas(login_frame, width=450, height=2.0, bg=fnt, highlightthickness=0)
    passwd_line.place(x=120, y=478)


    #--------------------"Sign in and Password icons"-------------------------------------------------------
   
   
    username_img=tk.PhotoImage(file=('D:/trela/Images/userr-icon.png'))    
    user_logo_lbl=tk.Label(login_frame,image=username_img)
    user_logo_lbl.image=username_img
    user_logo_lbl.place(x=88, y=342)


    passwd_img=tk.PhotoImage(file=('D:/trela/Images/pwd_icon.png'))    
    passwd_logo_lbl=tk.Label(login_frame,image=passwd_img)
    passwd_logo_lbl.image=passwd_img
    passwd_logo_lbl.place(x=88, y=450)


    #--------------------"Login Button"-------------------------------------------------------


    btn_img=tk.PhotoImage(file=('D:/trela/Images/btn.png'))    
    login_btn_img=tk.Label(login_frame,image=btn_img)
    login_btn_img.image=btn_img
    login_btn_img.place(x=225, y=510)

    login_btn=tk.Button(login_btn_img, text='Sign in', font=('yu gothic ui', 18, 'bold'),width=10, bd=0, highlightthickness=0,  bg=btn_bg, cursor='hand2', activebackground=btn_bg, fg='white', command=login_backend)
    login_btn.place(x=30, y=8)


    #--------------------"Signup Label"-------------------------------------------------------


    sign_up_label=tk.Button(login_frame, text='Not registered yet? Sign Up', font=('yu gothic ui', 18, 'bold underline'),background=th_clr, foreground=fnt, activebackground=th_clr,cursor='hand2', bd=0, width=20, command=signup_link)
    sign_up_label.place(x=185, y=570)

    #--------------------"Hide/Unhide Option"----------------------------------------------------------

    
    def show():
        hide_btn=tk.Button(login_frame, image=hide_img,command=hide, bg=th_clr, activebackground=th_clr, cursor='hand2', bd=0)
        hide_btn.place(x=537, y=450)    
        passwd_entry.config(show='')
    
    def hide():
        view_btn=tk.Button(login_frame, image=view_img, command=show, bg=th_clr, activebackground=th_clr, cursor='hand2', bd=0)
        view_btn.place(x=537, y=450)    
        passwd_entry.config(show='*')

    view_img=ImageTk.PhotoImage(Image.open('D:/trela/Images/view_pwd.png'))
    hide_img=ImageTk.PhotoImage(Image.open('D:/trela/Images/hide_pwd.png'))
    
    view_btn=tk.Button(login_frame, image=view_img, command=show, bg=th_clr, activebackground=th_clr, cursor='hand2', bd=0)
    view_btn.place(x=537, y=490)    

login_frontend()
login.mainloop() 