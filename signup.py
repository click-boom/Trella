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
 
 
    login_frame=tk.Frame(login, width='700', height='740',background=th_clr)   
    login_frame.place(x=620, y=220)


    #--------------------"Welcome To TRELLA and Sign Up label"-------------------------------------------------------------
 
 
    login.txt='Welcome To Trella'
    login.heading=tk.Label(login, 
     text=login.txt,
     font=('yu gothic ui', '30', 'bold'),
     fg='#6c6c6c',background=th_clr).place(x=780, y=420, width=400, height=50)


    #-----------------------------------"Logo"-------------------------------------------------------------
 
 
    logo_img=tk.PhotoImage(file=('/home/wae/Documents/giri raj sir/Trella/Images/dlogo.png'))    
    logo_lbl=tk.Label(login_frame,image=logo_img,background=th_clr)
    logo_lbl.image=logo_img
    logo_lbl.place(x=288, y=15)


    #------------------------------"Sign Up and Password"---------------------------------------------------


    username_lbl=tk.Label(login_frame, text='Username', fg=fnt,background=th_clr, font=('yu gothic ui', 16, 'bold'))
    username_lbl.place(x=120, y=300)
    username_entry=tk.Entry(login_frame, highlightthickness=0, relief='flat', fg=fnt, bg=th_clr, font=('yu gothic ui', 13, 'bold'))
    username_entry.place(x=120, y=330, width=450)

    username_line=tk.Canvas(login_frame, width=400, height=2.0, bg=fnt, highlightthickness=0)
    username_line.place(x=120, y=358, width=450)

    email_lbl=tk.Label(login_frame, text='Email', fg='#6c6c6c',background=th_clr, font=('yu gothic ui', 16, 'bold'))
    email_lbl.place(x=120, y=375)
    email_entry=tk.Entry(login_frame, highlightthickness=0, relief='flat', fg=fnt, bg=th_clr,font=('yu gothic ui', 13, 'bold'))
    email_entry.place(x=120, y=407, width=450)

    email_line=tk.Canvas(login_frame, width=450, height=2.0, bg=fnt, highlightthickness=0)
    email_line.place(x=120, y=435)


    epasswd_lbl=tk.Label(login_frame, text='Enter Password', fg='#6c6c6c', bg=th_clr, font=('yu gothic ui', 16, 'bold'))
    epasswd_lbl.place(x=120, y=452)
    epasswd_entry=tk.Entry(login_frame, highlightthickness=0, relief='flat', fg=fnt, bg=th_clr,font=('yu gothic ui', 13, 'bold'))
    epasswd_entry.place(x=120, y=485, width=450)

    epasswd_line=tk.Canvas(login_frame, width=450, height=2.0, bg=fnt, highlightthickness=0)
    epasswd_line.place(x=120, y=514)
    
    cpasswd_lbl=tk.Label(login_frame, text='Confirm Password', fg='#6c6c6c', bg=th_clr, font=('yu gothic ui', 16, 'bold'))
    cpasswd_lbl.place(x=120, y=530)
    cpasswd_entry=tk.Entry(login_frame, highlightthickness=0, relief='flat', fg=fnt, bg=th_clr,font=('yu gothic ui', 13, 'bold'))
    cpasswd_entry.place(x=120, y=565, width=450)

    cpasswd_line=tk.Canvas(login_frame, width=450, height=2.0, bg=fnt, highlightthickness=0)
    cpasswd_line.place(x=120, y=593)


    #--------------------"Sign in/ Email and Password icons"-------------------------------------------------------
   
   
    username_img=tk.PhotoImage(file='/home/wae/Documents/giri raj sir/Trella/Images/userr-icon.png')    
    user_logo_lbl=tk.Label(login_frame,bg=th_clr ,image=username_img)
    user_logo_lbl.image=username_img
    user_logo_lbl.place(x=85, y=327)

    email_img=tk.PhotoImage(file='/home/wae/Documents/giri raj sir/Trella/Images/mail.png')    
    user_logo_lbl=tk.Label(login_frame,bg=th_clr ,image=email_img)
    user_logo_lbl.image=email_img
    user_logo_lbl.place(x=85, y=407)

    passwd_img=tk.PhotoImage(file=('/home/wae/Documents/giri raj sir/Trella/Images/pwd_icon.png'))    
    passwd_logo_lbl=tk.Label(login_frame,bg=th_clr ,image=passwd_img)
    passwd_logo_lbl.image=passwd_img
    passwd_logo_lbl.place(x=85, y=490)


    passwd_img=tk.PhotoImage(file=('/home/wae/Documents/giri raj sir/Trella/Images/pwd_icon.png'))    
    passwd_logo_lbl=tk.Label(login_frame,bg=th_clr ,image=passwd_img)
    passwd_logo_lbl.image=passwd_img
    passwd_logo_lbl.place(x=85, y=568)


    # --------------------"Sign Up Button"-------------------------------------------------------
   
   
    btn_img=tk.PhotoImage(file=('/home/wae/Documents/giri raj sir/Trella/Images/btn.png'))    
    sgnup_btn_img=tk.Label(login_frame,image=btn_img)
    sgnup_btn_img.image=btn_img
    sgnup_btn_img.place(x=225, y=610)

    login_btn=tk.Button(sgnup_btn_img, text='Sign Up', font=('yu gothic ui', 18, 'bold'),width=10, bd=0, highlightthickness=0,  bg=btn_bg, cursor='hand2', activebackground=btn_bg, fg='white' )
    login_btn.place(x=30, y=8)


    # --------------------"Login Label"-------------------------------------------------------


    sign_up_label=tk.Button(login_frame, text='Already Registered? Login ', font=('yu gothic ui', 18, 'bold underline'),background=th_clr, foreground=fnt, activebackground=th_clr,cursor='hand2', bd=0, width=20)
    sign_up_label.place(x=185, y=670)


    #--------------------"Hide/Unhide Button"-------------------------------------------------------


    def ehide():
        eview_btn=tk.Button(login_frame, image=eview_img, command=eshow, bg=th_clr, activebackground=th_clr, cursor='hand2', bd=0)
        eview_btn.place(x=537, y=485)    
        epasswd_entry.config(show='*')
        
      
    def eshow():
        ehide_btn=tk.Button(login_frame, image=ehide_img,command=ehide, bg=th_clr, activebackground=th_clr, cursor='hand2', bd=0)
        ehide_btn.place(x=537, y=485)    
        epasswd_entry.config(show='')
        
        
    def chide(): 
        cview_btn=tk.Button(login_frame, image=cview_img, command=cshow, bg=th_clr, activebackground=th_clr, cursor='hand2', bd=0)
        cview_btn.place(x=537, y=565)    
        cpasswd_entry.config(show='*')

    def cshow():
        ehide_btn=tk.Button(login_frame, image=chide_img,command=chide, bg=th_clr, activebackground=th_clr, cursor='hand2', bd=0)
        ehide_btn.place(x=537, y=565)    
        epasswd_entry.config(show='')

    eview_img=ImageTk.PhotoImage(Image.open('/home/wae/Documents/giri raj sir/Trella/Images/view_pwd.png'))
    cview_img=ImageTk.PhotoImage(Image.open('/home/wae/Documents/giri raj sir/Trella/Images/view_pwd.png'))
    
    ehide_img=ImageTk.PhotoImage(Image.open('/home/wae/Documents/giri raj sir/Trella/Images/hide_pwd.png'))
    chide_img=ImageTk.PhotoImage(Image.open('/home/wae/Documents/giri raj sir/Trella/Images/hide_pwd.png'))
    
    eview_btn=tk.Button(login_frame, image=ehide_img, command=ehide, bg=th_clr, activebackground=th_clr, cursor='hand2', bd=0)
    eview_btn.place(x=537, y=485)    
    
    cview_btn=tk.Button(login_frame, image=chide_img, command=chide, bg=th_clr, activebackground=th_clr, cursor='hand2', bd=0)
    cview_btn.place(x=537, y=565)    

signup()
login.mainloop() 