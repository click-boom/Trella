import tkinter as tk
from PIL import ImageTk, Image
from tkinter import ttk
login=tk.Tk()


def loginpage():
    
    #--------------------Login Window------------------------------------------------------------
    
    # screen_width = win.winfo_screenwidth()
    # screen_height = win.winfo_screenheight()
    
    login.title('Welcome to Trella')
    login.geometry('1920x1080')
    login.minsize(1920,1080)


    #--------------------Functions---------------------------------------------------------------
    
    th_clr='#93cbff'
    fnt='#6c6c6c'
    def eye_hidden():
        if  login.passwd_entry.cget("show")=="*":
            login.passwd_entry.config(show="")

        else:
            login.passwd_entry.config(show="*") 



    #--------------------Page Background-------------------------------------------------------------
    img=ImageTk.PhotoImage(Image.open('/home/wae/Documents/giri raj sir/Trella/rohan.png'))
    bg=tk.Label(login, image=img)
    bg.image=img
    bg.pack(fill='both', expand='yes')


    #--------------------Login Frame-------------------------------------------------------------
    login_frame=tk.Frame(login, width='700', bg=th_clr,height='700')
    login_frame.place(x=620, y=220)


    #--------------------"Welcome To TRELLA"-------------------------------------------------------------
    login.txt='Welcome To Trella'
    login.heading=tk.Label(login, 
     text=login.txt,
     font=('yu gothic ui', '30', 'bold'),
     fg='#6c6c6c',
     bg=th_clr).place(x=780, y=435, width=400, height=50)


    #-----------------------------------"Logo"-------------------------------------------------------------
    logo_img=tk.PhotoImage(file=('/home/wae/Documents/giri raj sir/Trella/llogo.png'))    
    login.logo_lbl=tk.Label(login_frame,image=logo_img, bg=th_clr)
    login.logo_lbl.image=logo_img
    login.logo_lbl.place(x=288, y=25)


    #------------------------------"Sign in and Password"---------------------------------------------------


    login.username_lbl=tk.Label(login_frame, text='Username', fg=fnt,bg=th_clr, font=('yu gothic ui', 18, 'bold'))
    login.username_lbl.place(x=120, y=300)
    login.username_entry=tk.Entry(login_frame, highlightthickness=0, relief='flat', fg=fnt, bg=th_clr, font=('yu gothic ui', 15, 'bold'))
    login.username_entry.place(x=120, y=340, width=450)

    login.username_line=tk.Canvas(login_frame, width=400, height=3.0, bg=fnt, highlightthickness=0)
    login.username_line.place(x=120, y=370, width=450)

    login.passwd_lbl=tk.Label(login_frame, text='Password', fg='#6c6c6c', bg=th_clr, font=('yu gothic ui', 18, 'bold'))
    login.passwd_lbl.place(x=120, y=410)
    login.passwd_entry=tk.Entry(login_frame, highlightthickness=0, relief='flat', fg=fnt, bg=th_clr,show="*",font=('yu gothic ui', 15, 'bold'))
    login.passwd_entry.place(x=120, y=450, width=450)

    login.password_line=tk.Canvas(login_frame, width=450, height=2.0, bg=fnt, highlightthickness=0)
    login.password_line.place(x=120, y=478)

    #--------------------"Sign in and Password icons"-------------------------------------------------------
   
   
    username_img=tk.PhotoImage(file=('/home/wae/Documents/giri raj sir/Trella/userr-icon.png'))    
    login.user_logo_lbl=tk.Label(login_frame,bg=th_clr,image=username_img)
    login.user_logo_lbl.image=username_img
    login.user_logo_lbl.place(x=88, y=342)


    passwd_img=tk.PhotoImage(file=('/home/wae/Documents/giri raj sir/Trella/pwd_icon.png'))    
    login.passwd_logo_lbl=tk.Label(login_frame,bg=th_clr,image=passwd_img)
    login.passwd_logo_lbl.image=passwd_img
    login.passwd_logo_lbl.place(x=88, y=450)


    #--------------------"Password Eye Button"-------------------------------------------------------
    img=tk.PhotoImage(file="/home/wae/Documents/giri raj sir/Trella/hide_pwd.png")
    img_lable=tk.Label(login_frame,image=img)
    
    img_lable.place(x=800,y=500)

    show_button=tk.Button(login_frame,text="show",activebackground="black",bd=0,background="grey",command=eye_hidden)
    show_button.place(x=500,y=445)








    
    
    
    
    #--------------------"Login Button"-------------------------------------------------------
    # login.login_btn=ImageTk.PhotoImage(Image.open(''))
loginpage()
login.mainloop() 