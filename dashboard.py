import tkinter as tk
from PIL import ImageTk, Image

dash=tk.Tk()
dash.title('TRELLA')
dash.geometry('1920x1080')
dash.minsize(1920, 1080)

icon=tk.PhotoImage(file='/home/wae/Documents/giri raj sir/Trella/Images/llogo.png')
dash .iconphoto(True, icon)

#========================BACK END======================================
def dash_backend():
    pass

#========================FRONT END======================================
#-------------------  Theme  -----------------------------
            
lth_clr='#A0B6E9'
dth_clr='#4C6195'
btn_bg='#637EC2'

lfnt=lth_clr
dfnt=dth_clr

#----------------------------------------------------------
def dash_frontend():
#------------------  HEADER BAR ---------------------------

    header= tk.Frame(dash , bg=lth_clr)
    header.place(x=400, y=0, width=1550, height=150)   

#------------------  SIDEBAR  ---------------------------
    sidebar =tk.Frame(dash ,bg=dth_clr)    
    sidebar.place(x=0, y=0, width=400, height=1080)
#----------------  Dashboard Heading  -------------------
    heading =tk.Label(header , text='Dashboard',font=('yu gothic ui', 44, 'bold'),bg=lth_clr, fg=dfnt)
    heading.place(x=600, y=35)
        
#----------------  Logo Frame  -------------------
    
    lframe =tk.Frame(sidebar ,bg=dth_clr)    
    lframe.place(x=50, y=50, width=300, height=250)

    #----------------  Logo Image -------------------
    
    dash_logo=ImageTk.PhotoImage(Image.open('/home/wae/Documents/giri raj sir/Trella/Images/llogo.png'))
    logo_lbl=tk.Label(lframe, image=dash_logo, bg= dth_clr)
    logo_lbl.image=dash_logo
    logo_lbl.pack(side='top') 
    
    #----------------  Logo Label -------------------

    logo_lbl=tk.Label(lframe, text='Hello Haseena', bg= dth_clr, font=('yu gothic ui', 25, 'bold'), fg=lfnt)
    logo_lbl.image=dash_logo
    logo_lbl.pack(side='bottom') 

# ====================  Button Labels  ========================
    #-----------------Checklist--------------------------
    btn_img=tk.PhotoImage(file='/home/wae/Documents/giri raj sir/Trella/Images/dash_btn.png')
    
    chk_btn_lbl=tk.Label(sidebar, image=btn_img, bg=dth_clr)
    chk_btn_lbl.image=btn_img
    chk_btn_lbl.place(x=15, y=370)

    #-----------------  REMINDER  --------------------------
    
    rem_btn_lbl=tk.Label(sidebar, image=btn_img, bg=dth_clr)
    rem_btn_lbl.image=btn_img
    rem_btn_lbl.place(x=15, y=460)

    #-----------------  sticky notes  --------------------------
        
    st_btn_lbl=tk.Label(sidebar, image=btn_img, bg=dth_clr)
    st_btn_lbl.image=btn_img
    st_btn_lbl.place(x=15, y=550)

    #-----------------  Calendar  --------------------------
    
    cal_btn_lbl=tk.Label(sidebar, image=btn_img, bg=dth_clr)
    cal_btn_lbl.image=btn_img
    cal_btn_lbl.place(x=15, y=640)

# ====================  Buttons  ==============================
    #-----------------  Checklist  --------------------------
    
    chk_img=ImageTk.PhotoImage(Image.open('/home/wae/Documents/giri raj sir/Trella/Images/check-list.png'))
    chk_img.image=chk_img
    chk_btn=tk.Button(chk_btn_lbl, text='          CHECKLIST',font=('yu gothic ui', 25, 'bold'), bg=btn_bg, fg=lfnt, cursor='hand2', activebackground=btn_bg, bd=0,highlightthickness=0 )
    chk_btn.place(x=30, y=7)

    chk_img_lbl=tk.Label(chk_btn, image=chk_img, bg=btn_bg)
    chk_img_lbl.place(x=10, y=10)
    
    #-----------------  reminder  --------------------------
    
    rem_img=ImageTk.PhotoImage(Image.open('/home/wae/Documents/giri raj sir/Trella/Images/reminder.png'))
    rem_img.image=rem_img
    rem_btn=tk.Button(rem_btn_lbl, text='          REMINDER',font=('yu gothic ui', 25, 'bold'), bg=btn_bg, fg=lfnt, cursor='hand2', activebackground=btn_bg, bd=0,highlightthickness=0 )
    rem_btn.place(x=30, y=10)

    rem_img_lbl=tk.Label(rem_btn, image=rem_img, bg=btn_bg)
    rem_img_lbl.place(x=10, y=10)

    #-----------------  sticky notes --------------------------
    
    st_img=ImageTk.PhotoImage(Image.open('/home/wae/Documents/giri raj sir/Trella/Images/reminder.png'))
    st_img.image=st_img
    st_btn=tk.Button(st_btn_lbl, text='       STICKY NOTES',font=('yu gothic ui', 25, 'bold'), bg=btn_bg, fg=lfnt, cursor='hand2', activebackground=btn_bg, bd=0,highlightthickness=0 )
    st_btn.place(x=30, y=10)

    st_img_lbl=tk.Label(st_btn, image=st_img, bg=btn_bg)
    st_img_lbl.place(x=10, y=10)

    #-----------------  Calendar  --------------------------
    
    cal_img=ImageTk.PhotoImage(Image.open('/home/wae/Documents/giri raj sir/Trella/Images/calendar.png'))
    cal_img.image=cal_img
    cal_btn=tk.Button(cal_btn_lbl, text='         CALENDAR',font=('yu gothic ui', 25, 'bold'), bg=btn_bg, fg=lfnt, cursor='hand2', activebackground=btn_bg, bd=0,highlightthickness=0)
    cal_btn.place(x=30, y=10)

    cal_img_lbl=tk.Label(cal_btn, image=cal_img, bg=btn_bg)
    cal_img_lbl.place(x=10, y=10)

#-----------------  Logout Button  --------------------------

    lcircle_img=tk.PhotoImage(file='/home/wae/Documents/giri raj sir/Trella/Images/l_btn.png')
    lcircle_img.image=lcircle_img
    lcircle_lbl=tk.Label(sidebar, image=lcircle_img, bg=dth_clr)
    lcircle_lbl.place(x=135, y=850)

    lbtn_img=tk.PhotoImage(file='/home/wae/Documents/giri raj sir/Trella/Images/logout.png')
    lbtn_img.image=lbtn_img
    lbtn=tk.Button(lcircle_lbl, image=lbtn_img, bg=btn_bg, activebackground=btn_bg, cursor='hand2', highlightthickness=0, bd=0)
    lbtn.place(x=19, y=15)

dash_frontend()

dash.mainloop()