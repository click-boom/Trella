import tkinter as tk
from PIL import ImageTk, Image

dash=tk.Tk()
dash.title('TRELLA')
dash.geometry('1920x1080')
dash.minsize(1920, 1080)

icon=tk.PhotoImage(file='D:/Trella/Images/llogo.png')
dash .iconphoto(True, icon)
#========================FRONT END======================================
#-------------------  Theme  -----------------------------
            
lth_clr='#97C1EC'
dth_clr='#2A5F7F'
btn_bg='#5B90B4'
frm_clr='#A4c8Eb'

lfnt=lth_clr
dfnt=dth_clr

def checklist_link():
    dash.destroy()
    import checklist11

def reem_link():
    dash.destory()
    import reminder

def stickk_notees():
    dash.destroy()
    import Stickynotes

# def button_hover(e):
#     text_button.config(text="Search")

#----------------------------------------------------------
def chk_frontend():
    dashfr=tk.Frame(dash, width=1230, height=76)
    # dashfr.config(bg=lth_clr)
    dashfr.place(x=535, y=300)
    
    dashfr_img=ImageTk.PhotoImage(Image.open('D:/Trella/Images/dash_bg.jpg'))
    dash_bg=tk.Label(dash, image=dashfr_img)
    dash_bg.image=dashfr_img
    dash_bg.pack(fill='both', expand='yes')

#------------------  SIDEBAR  ---------------------------
    sidebar =tk.Frame(dash ,bg=dth_clr)    
    sidebar.place(x=30, y=70, width=400, height=800)
#----------------  Dashboard Heading  -------------------
        
#----------------  Logo Frame  -------------------
    
    lframe =tk.Frame(sidebar ,bg=dth_clr)    
    lframe.place(x=50, y=50, width=300, height=250)

    #----------------  Logo Image -------------------
    
    dash_logo=ImageTk.PhotoImage(Image.open('D:/Trella/Images/llogo.png'))
    logo_lbl=tk.Label(lframe, image=dash_logo, bg= dth_clr)
    logo_lbl.image=dash_logo
    logo_lbl.pack(side='top') 
    
    #----------------  Logo Label -------------------

    logo_lbl=tk.Label(lframe, text='Hello Haseena', bg= dth_clr, font=('yu gothic ui', 25, 'bold'), fg=lfnt)
    logo_lbl.image=dash_logo
    logo_lbl.pack(side='bottom') 

# ====================  Button Labels  ========================
    #-----------------Checklist--------------------------
    btn_img=tk.PhotoImage(file='D:/Trella/Images/DASH_BTN.png')
    
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

# ====================  Buttons  ==============================
    #-----------------  Checklist  --------------------------


    
    chk_img=ImageTk.PhotoImage(Image.open('D:/Trella/Images/check-list.png'))
    chk_img.image=chk_img
    chk_btn=tk.Button(chk_btn_lbl, text='          CHECKLIST',font=('yu gothic ui', 25, 'bold'), bg=btn_bg, fg=lfnt, cursor='hand2', activebackground=btn_bg,activeforeground='white', bd=0,highlightthickness=0,command=checklist_link)
    chk_btn.place(x=30, y=7)

    chk_img_lbl=tk.Label(chk_btn, image=chk_img, bg=btn_bg)
    chk_img_lbl.place(x=10, y=10)

    
    #-----------------  reminder  --------------------------
    
    rem_img=ImageTk.PhotoImage(Image.open('D:/Trella/Images/check-list.png'))
    rem_img.image=rem_img
    rem_btn=tk.Button(rem_btn_lbl, text='          REMINDER',font=('yu gothic ui', 25, 'bold'), bg=btn_bg, fg='white', cursor='hand2', activebackground=btn_bg, activeforeground='white',bd=0,highlightthickness=0 ,command=reem_link)
    rem_btn.place(x=30, y=10)

    rem_img_lbl=tk.Label(rem_btn, image=rem_img, bg=btn_bg)
    rem_img_lbl.place(x=10, y=10)

    #-----------------  sticky notes --------------------------
    
    st_img=ImageTk.PhotoImage(Image.open('D:/Trella/Images/check-list.png'))
    st_img.image=st_img
    st_btn=tk.Button(st_btn_lbl, text='       STICKY NOTES',font=('yu gothic ui', 25, 'bold'), bg=btn_bg, fg=lfnt, cursor='hand2', activebackground=btn_bg,activeforeground='white', bd=0,highlightthickness=0 ,command=stickk_notees)
    st_btn.place(x=30, y=10)

    st_img_lbl=tk.Label(st_btn, image=st_img, bg=btn_bg)
    st_img_lbl.place(x=10, y=10)


#-----------------  Logout Button  --------------------------

    lcircle_img=tk.PhotoImage(file='D:/Trella/Images/L_BTN.png')
    lcircle_img.image=lcircle_img
    lcircle_lbl=tk.Label(sidebar, image=lcircle_img, bg=dth_clr)
    lcircle_lbl.place(x=135, y=650)

    lbtn_img=tk.PhotoImage(file='D:/Trella/Images/logout.png')
    lbtn_img.image=lbtn_img
    lbtn=tk.Button(lcircle_lbl, image=lbtn_img, bg=btn_bg, activebackground=btn_bg, cursor='hand2', highlightthickness=0, bd=0)
    lbtn.place(x=19, y=15)

#----------------  Reminder  Frame  -------------------------------
    rem_frame =tk.Frame(dash ,bg=frm_clr)    
    rem_frame.place(x=470, y=120, width=1390, height=860)

    heading =tk.Label(dash, text='Reminder',font=('yu gothic ui', 45, 'bold'),bg="#95C3EA", fg=dfnt)
    heading.place(x=970,y=30)  

    # three_dash_img=ImageTk.PhotoImage(file='D:\Trella\Images\list.png')
    # three_dash_img.image=three_dash_img
    # three_dash=tk.Button(rem_frame,image=three_dash_img,cursor="hand2", bd=0,background=frm_clr,activebackground=frm_clr)
    # three_dash.place(x=50,y=55)

#-------------------------search button-------------------------------------
    search_imge=ImageTk.PhotoImage(file='D:\Trella\Images\search.png')
    search_imge.image=search_imge
    search_Button=tk.Button(rem_frame,image=search_imge ,cursor="hand2",bd=0,background=frm_clr,activebackground=frm_clr)
    search_Button.place(x=930,y=61)

    search_bar_img=ImageTk.PhotoImage(file='D:/Trella/Images/hbar.png')
    search_lbl=tk.Label(rem_frame, image=search_bar_img, bg=frm_clr)
    search_lbl.image=search_bar_img
    search_lbl.place(x=960, y=47)

    search_box=tk.Entry(search_lbl,font=('yu gothic ui', 14, 'bold'),background="#5B90B4", width=21,bd=0)
    search_box.place(x=15,y=10)




    #--------------------remind me-----------------------
    remind_img=ImageTk.PhotoImage(file='D:/Trella/Images/alarm.png')
    remind_img.image=remind_img
    remind_img_mutton=tk.Button(rem_frame,image=remind_img ,cursor="hand2",bd=0,background=frm_clr,activebackground=frm_clr)
    remind_img_mutton.place(x=50,y=160)

    remind_bar_img=ImageTk.PhotoImage(file='D:/Trella/Images/hbar.png')
    remind_lbl=tk.Label(rem_frame, image=remind_bar_img, bg=frm_clr)
    remind_lbl.image=remind_bar_img
    remind_lbl.place(x=90, y=160)
    
    remind_button=tk.Button(remind_lbl,text="Remind me",font=('yu gothic ui', 12, 'bold'),bg='#98BAD4',fg=dfnt,bd=0,width=25,activebackground='#98BAD4')
    remind_button.pack()

    #^^^^^^^^^^^^^^^^^^Add text^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    add_text_img=ImageTk.PhotoImage(file='D:/Trella/Images/calendar.png')
    add_text_img.image=add_text_img
    add_text_img_mutton=tk.Button(rem_frame,image=add_text_img ,cursor="hand2",bd=0,background=frm_clr,activebackground=frm_clr)
    add_text_img_mutton.place(x=50,y=210)

    add_text_bar_img=ImageTk.PhotoImage(file='D:/Trella/Images/hbar.png')
    add_text_lbl=tk.Label(rem_frame, image=add_text_bar_img, bg=frm_clr)
    add_text_lbl.image=add_text_bar_img
    add_text_lbl.place(x=90, y=210)
    
    add_text_button=tk.Button(add_text_lbl,text="Add text",font=('yu gothic ui', 12, 'bold'),bg='#98BAD4',fg=dfnt,bd=0,width=25,activebackground='#98BAD4')
    add_text_button.pack()

    #--------------------------Add to my day---------------------------
    add_day_img=ImageTk.PhotoImage(file='D:/Trella/Images/sun (1).png')
    add_day_img.image=add_day_img
    add_day_img_mutton=tk.Button(rem_frame,image=add_day_img ,cursor="hand2",bd=0,background=frm_clr,activebackground=frm_clr)
    add_day_img_mutton.place(x=50,y=260)

    add_day_bar_img=ImageTk.PhotoImage(file='D:/Trella/Images/hbar.png')
    add_day_lbl=tk.Label(rem_frame, image=add_day_bar_img, bg=frm_clr)
    add_day_lbl.image=add_day_bar_img
    add_day_lbl.place(x=90, y=260)
    
    add_day_button=tk.Button(add_day_lbl,text="Add to my day",font=('yu gothic ui', 12, 'bold'),bg='#98BAD4',fg=dfnt,bd=0,width=25,activebackground='#98BAD4')
    add_day_button.pack()

#------------------------add to due date---------------------------
    add_date_img=ImageTk.PhotoImage(file='D:/Trella/Images/calendar (1).png')
    add_date_img.image=add_date_img
    add_date_img_mutton=tk.Button(rem_frame,image=add_date_img ,cursor="hand2",bd=0,background=frm_clr,activebackground=frm_clr)
    add_date_img_mutton.place(x=49, y=315)

    add_date_bar_img=ImageTk.PhotoImage(file='D:/Trella/Images/hbar.png')
    add_date_lbl=tk.Label(rem_frame, image=add_date_bar_img, bg=frm_clr)
    add_date_lbl.image=add_date_bar_img
    add_date_lbl.place(x=90, y=310)
    
    add_date_button=tk.Button(add_date_lbl,text="Add to due date",font=('yu gothic ui', 11, 'bold'),bg='#98BAD4',fg=dfnt,bd=0,width=25,activebackground='#98BAD4')
    add_date_button.pack()
    
 #------------------------repeat---------------------------
    repeat_img=ImageTk.PhotoImage(file='D:/Trella/Images/repeat12.png')
    repeat_img.image=repeat_img
    repeat_img_button=tk.Button(rem_frame,image=repeat_img ,cursor="hand2",bd=0,background=frm_clr,activebackground=frm_clr)
    repeat_img_button.place(x=50,y=360)

    repeat_bar_img=ImageTk.PhotoImage(file='D:/Trella/Images/hbar.png')
    repeat_lbl=tk.Label(rem_frame, image=repeat_bar_img, bg=frm_clr)
    repeat_lbl.image=repeat_bar_img
    repeat_lbl.place(x=90, y=360)
    
    repeat_button=tk.Button(repeat_lbl,text="Repeat",font=('yu gothic ui', 12, 'bold'),bg='#98BAD4',fg=dfnt,bd=0,width=25,activebackground='#98BAD4')
    repeat_button.pack()


#------------------------Attach---------------------------
    Attach_img=ImageTk.PhotoImage(file='D:/Trella/Images/attached (1).png')
    Attach_img.image=Attach_img
    Attach_img_button=tk.Button(rem_frame,image=Attach_img ,cursor="hand2",bd=0,background=frm_clr,activebackground=frm_clr)
    Attach_img_button.place(x=50,y=410)

    Attach_bar_img=ImageTk.PhotoImage(file='D:/Trella/Images/hbar.png')
    Attach_lbl=tk.Label(rem_frame, image=Attach_bar_img, bg=frm_clr)
    Attach_lbl.image=Attach_bar_img
    Attach_lbl.place(x=90, y=410)
    
    Attach_button=tk.Button(Attach_lbl,text="Attach",font=('yu gothic ui', 12, 'bold'),bg='#98BAD4',fg=dfnt,bd=0,width=25,activebackground='#98BAD4')
    Attach_button.pack()

    













chk_frontend()

dash.mainloop()
