import tkinter as tk
from PIL import ImageTk, Image
from tkinter import ttk
login=tk.Tk()


def signup():
    
    #--------------------Login Window-------------------------------------------------------------
    
    # screen_width = win.winfo_screenwidth()
    # screen_height = win.winfo_screenheight()
    
    login.title('Welcome to Trella')
    login.geometry('1920x1080')
    login.resizable(1, 1)


    #--------------------Functions---------------------------------------------------------------
    
    th_clr='#d6d6d6'
    fnt='#6c6c6c'
    btn_bg='#a4a4a4'

    #--------------------Page Background-------------------------------------------------------------
    img=ImageTk.PhotoImage(Image.open('/home/wae/Documents/giri raj sir/Trella/SignUp/bg.png'))
    bg=tk.Label(login, image=img)
    bg.image=img
    bg.pack(fill='both', expand='yes')


    #--------------------Login Frame-------------------------------------------------------------
    login_frame=tk.Frame(login, width='700', height='740',background=th_clr)   
    login_frame.place(x=620, y=220)


    #--------------------"Welcome To TRELLA and Sign Up label"-------------------------------------------------------------
    login.txt='Welcome To Trella'
    login.heading=tk.Label(login, 
     text=login.txt,
     font=('yu gothic ui', '30', 'bold'),
     fg='#6c6c6c',background=th_clr).place(x=780, y=420, width=400, height=50)


    #-----------------------------------"Logo"-------------------------------------------------------------
    logo_img=tk.PhotoImage(file=('/home/wae/Documents/giri raj sir/Trella/SignUp/dlogo.png'))    
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
    login.email_entry.place(x=120, y=407, width=450)

    login.email_line=tk.Canvas(login_frame, width=450, height=2.0, bg=fnt, highlightthickness=0)
    login.email_line.place(x=120, y=435)


    login.epasswd_lbl=tk.Label(login_frame, text='Enter Password', fg='#6c6c6c', bg=th_clr, font=('yu gothic ui', 16, 'bold'))
    login.epasswd_lbl.place(x=120, y=452)
    login.epasswd_entry=tk.Entry(login_frame, highlightthickness=0, relief='flat', fg=fnt, bg=th_clr,show="*",font=('yu gothic ui', 13, 'bold'))
    login.epasswd_entry.place(x=120, y=485, width=450)

    login.epasswd_line=tk.Canvas(login_frame, width=450, height=2.0, bg=fnt, highlightthickness=0)
    login.epasswd_line.place(x=120, y=514)
    
    login.cpasswd_lbl=tk.Label(login_frame, text='Confirm Password', fg='#6c6c6c', bg=th_clr, font=('yu gothic ui', 16, 'bold'))
    login.cpasswd_lbl.place(x=120, y=530)
    login.cpasswd_entry=tk.Entry(login_frame, highlightthickness=0, relief='flat', fg=fnt, bg=th_clr,show="*",font=('yu gothic ui', 13, 'bold'))
    login.cpasswd_entry.place(x=120, y=565, width=450)

    login.cpasswd_line=tk.Canvas(login_frame, width=450, height=2.0, bg=fnt, highlightthickness=0)
    login.cpasswd_line.place(x=120, y=593)


    #--------------------"Sign in/ Email and Password icons"-------------------------------------------------------
   
   
    username_img=tk.PhotoImage(file='/home/wae/Documents/giri raj sir/Trella/SignUp/userr-icon.png')    
    login.user_logo_lbl=tk.Label(login_frame,bg=th_clr ,image=username_img)
    login.user_logo_lbl.image=username_img
    login.user_logo_lbl.place(x=85, y=327)

    email_img=tk.PhotoImage(file='/home/wae/Documents/giri raj sir/Trella/SignUp/mail.png')    
    login.user_logo_lbl=tk.Label(login_frame,bg=th_clr ,image=email_img)
    login.user_logo_lbl.image=email_img
    login.user_logo_lbl.place(x=85, y=407)

    passwd_img=tk.PhotoImage(file=('/home/wae/Documents/giri raj sir/Trella/SignUp/pwd_icon.png'))    
    login.passwd_logo_lbl=tk.Label(login_frame,bg=th_clr ,image=passwd_img)
    login.passwd_logo_lbl.image=passwd_img
    login.passwd_logo_lbl.place(x=85, y=490)


    passwd_img=tk.PhotoImage(file=('/home/wae/Documents/giri raj sir/Trella/SignUp/pwd_icon.png'))    
    login.passwd_logo_lbl=tk.Label(login_frame,bg=th_clr ,image=passwd_img)
    login.passwd_logo_lbl.image=passwd_img
    login.passwd_logo_lbl.place(x=85, y=568)


    # --------------------"Sign Up Button"-------------------------------------------------------
   
   
    btn_img=tk.PhotoImage(file=('/home/wae/Documents/giri raj sir/Trella/SignUp/btn.png'))    
    login.sgnup_btn_img=tk.Label(login_frame,image=btn_img)
    login.sgnup_btn_img.image=btn_img
    login.sgnup_btn_img.place(x=225, y=610)

    login_btn=tk.Button(login.sgnup_btn_img, text='Sign Up', font=('yu gothic ui', 18, 'bold'),width=10, bd=0, highlightthickness=0,  bg=btn_bg, cursor='hand2', activebackground=btn_bg, fg='white' )
    login_btn.place(x=30, y=8)


    # --------------------"Login Label"-------------------------------------------------------


    login.sign_up_label=tk.Button(login_frame, text='Already Registered? Login ', font=('yu gothic ui', 18, 'bold underline'),background=th_clr, foreground=fnt, activebackground=th_clr,cursor='hand2', bd=0, width=20)
    login.sign_up_label.place(x=185, y=670)


    #--------------------"Password Eye Button"-------------------------------------------------------
signup()
login.mainloop() 