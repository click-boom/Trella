import tkinter as tk
from PIL import ImageTk, Image

dash=tk.Tk()
dash.title('TRELLA')
dash.geometry('1920x1080')
dash.minsize(1920, 1080)

icon=tk.PhotoImage(file='/home/wae/Documents/giri raj sir/Trella/Images/llogo.png')
dash .iconphoto(True, icon)
#========================FRONT END======================================
#-------------------  Theme  -----------------------------
            
lth_clr='#97C1EC'
dth_clr='#2A5F7F'
btn_bg='#5B90B4'

lfnt=lth_clr
dfnt=dth_clr

#----------------------------------------------------------
def chk_frontend():
    dashfr=tk.Frame(dash, width=1230, height=746)
    # dashfr.config(bg=lth_clr)
    dashfr.place(x=535, y=300)
    
    dashfr_img=ImageTk.PhotoImage(Image.open('/home/wae/Documents/giri raj sir/Trella/Images/1.jpg'))
    dash_bg=tk.Label(dash, image=dashfr_img)
    dash_bg.image=dashfr_img
    dash_bg.pack(fill='both', expand='yes')

#------------------  SIDEBAR  ---------------------------
    sidebar =tk.Frame(dash ,bg=dth_clr)    
    sidebar.place(x=30, y=70, width=400, height=800)
#----------------  Dashboard Heading  -------------------
    heading =tk.Label(dash , text='Dashboard',font=('yu gothic ui', 44, 'bold'),bg=lth_clr, fg=dfnt)
    heading.place(x=950, y=35)
        
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

# ====================  Buttons  ==============================
    #-----------------  Checklist  --------------------------
    
    chk_img=ImageTk.PhotoImage(Image.open('/home/wae/Documents/giri raj sir/Trella/Images/check-list.png'))
    chk_img.image=chk_img
    chk_btn=tk.Button(chk_btn_lbl, text='          CHECKLIST',font=('yu gothic ui', 25, 'bold'), bg=btn_bg, fg=lfnt, cursor='hand2', activebackground=btn_bg,activeforeground='white', bd=0,highlightthickness=0 )
    chk_btn.place(x=30, y=7)

    chk_img_lbl=tk.Label(chk_btn, image=chk_img, bg=btn_bg)
    chk_img_lbl.place(x=10, y=10)
    
    #-----------------  reminder  --------------------------
    
    rem_img=ImageTk.PhotoImage(Image.open('/home/wae/Documents/giri raj sir/Trella/Images/reminder.png'))
    rem_img.image=rem_img
    rem_btn=tk.Button(rem_btn_lbl, text='          REMINDER',font=('yu gothic ui', 25, 'bold'), bg=btn_bg, fg=lfnt, cursor='hand2', activebackground=btn_bg, activeforeground='white',bd=0,highlightthickness=0 )
    rem_btn.place(x=30, y=10)

    rem_img_lbl=tk.Label(rem_btn, image=rem_img, bg=btn_bg)
    rem_img_lbl.place(x=10, y=10)

    #-----------------  sticky notes --------------------------
    
    st_img=ImageTk.PhotoImage(Image.open('/home/wae/Documents/giri raj sir/Trella/Images/reminder.png'))
    st_img.image=st_img
    st_btn=tk.Button(st_btn_lbl, text='       STICKY NOTES',font=('yu gothic ui', 25, 'bold'), bg=btn_bg, fg='white', cursor='hand2', activebackground=btn_bg,activeforeground='white', bd=0,highlightthickness=0 )
    st_btn.place(x=30, y=10)

    st_img_lbl=tk.Label(st_btn, image=st_img, bg=btn_bg)
    st_img_lbl.place(x=10, y=10)

#-----------------  Logout Button  --------------------------

    lcircle_img=tk.PhotoImage(file='/home/wae/Documents/giri raj sir/Trella/Images/l_btn.png')
    lcircle_img.image=lcircle_img
    lcircle_lbl=tk.Label(sidebar, image=lcircle_img, bg=dth_clr)
    lcircle_lbl.place(x=135, y=670)

    lbtn_img=tk.PhotoImage(file='/home/wae/Documents/giri raj sir/Trella/Images/logout.png')
    lbtn_img.image=lbtn_img
    lbtn=tk.Button(lcircle_lbl, image=lbtn_img, bg=btn_bg, activebackground=btn_bg, cursor='hand2', highlightthickness=0, bd=0)
    lbtn.place(x=19, y=15)

#...................topic.........................



    
    side_line=tk.Canvas(dash, width=1400, height=70,
                                bg='#A4C8E8', 
                                highlightthickness=0)
    side_line.place(x=460, y=875)
    


# ...................create_button.........................
    create= tk.Button(dash, text='Create',
                                font=('yu gothic ui', 15, 'bold'),
                                bg='#2A5F7F',
                                bd=0,
                                cursor='hand2',
                                fg='#A4C8E8',
                                activebackground='#2A5F7F',
                                width='10'
                      )
    create.place(x=480, y=890)
    

    
# ...................A-icon.........................
    Aicon= Image.open('D://TRELLA/Images/A.png')
    
    photo = ImageTk.PhotoImage(Aicon)
    a=tk. Button(dash, 
                          image=photo,
                          bg='#A4C8E8',
                          bd=0,
                          cursor='hand2',
                          activebackground='#A4C8E8')
    a.image= photo
    a.place(x=650, y=888) 
    
    
    
    # Aicon=ImageTk.PhotoImage(file='D://TRELLA/Images/A.png')
    # Aicon.image=Aicon
    # Aicon_mutton=tk.Button(dash,image=Aicon ,cursor="hand2",bd=0,background='#A4C8E8',activebackground='#A4C8E8')
    # Aicon_mutton.place(x=650,y=957)



# ...................attach-icon.........................

    attachicon= Image.open('D://TRELLA/Images/attach.png')
    photo = ImageTk.PhotoImage(attachicon)
    attach=tk. Button(dash, 
                          image=photo,
                          bg='#A4C8E8',
                          bd=0,
                          cursor='hand2',
                          activebackground='#A4C8E8')
    attach.image= photo
    attach.place(x=720, y=890) 
    
# ...................insert-icon.........................

    inserticon= Image.open('D://TRELLA/Images/insert.png')
    photo = ImageTk.PhotoImage(inserticon)
    insert=tk. Button(dash, 
                          image=photo,
                          bg='#A4C8E8',
                          bd=0,
                          cursor='hand2',
                          activebackground='#A4C8E8')
    insert.image= photo
    insert.place(x=790, y=890) 

# ...................emoji-icon.........................

    emojiicon= Image.open('D://TRELLA/Images/emoji.png')
    photo = ImageTk.PhotoImage(emojiicon)
    emoji=tk. Button(dash, 
                          image=photo,
                          bg='#A4C8E8',
                          bd=0,
                          cursor='hand2',
                          activebackground='#A4C8E8')
    emoji.image= photo
    emoji.place(x=860, y=890) 
# ...................drive-icon.........................


    driveicon= Image.open('D://TRELLA/Images/drive.png')
    photo = ImageTk.PhotoImage(driveicon)
    drive=tk. Button(dash, 
                          image=photo,
                          bg='#A4C8E8',
                          bd=0,
                          cursor='hand2',
                          activebackground='#A4C8E8')
    drive.image= photo
    drive.place(x=930, y=890) 
# ...................gallery-icon.........................

    galleryicon= Image.open('D://TRELLA/Images/gallery.png')
    photo = ImageTk.PhotoImage(galleryicon)
    gallery=tk. Button(dash, 
                          image=photo,
                          bg='#A4C8E8',
                          bd=0,
                          cursor='hand2',
                          activebackground='#A4C8E8')
    gallery.image= photo
    gallery.place(x=1000, y=890) 


# ...................lock-icon.........................

    lockicon= Image.open('D://TRELLA/Images/lock.png')
    photo = ImageTk.PhotoImage(lockicon)
    lock=tk. Button(dash, 
                          image=photo,
                          bg='#A4C8E8',
                          bd=0,
                          cursor='hand2',
                          activebackground='#A4C8E8')
    lock.image= photo
    lock.place(x=1080, y=890) 
    
# ...................more-icon.........................

    moreicon= Image.open('D://TRELLA/Images/more.png')
    photo = ImageTk.PhotoImage(moreicon)
    more=tk. Button(dash, 
                          image=photo,
                          bg='#A4C8E8',
                          bd=0,
                          cursor='hand2',
                          activebackground='#A4C8E8')
    more.image= photo
    more.place(x=1140, y=890) 
# ...................delete-icon.........................


    deleteicon= Image.open('D://TRELLA/Images/delete.png')
    photo = ImageTk.PhotoImage(deleteicon)
    delete=tk. Button(dash, 
                          image=photo,
                          bg='#A4C8E8',
                          bd=0,
                          cursor='hand2',
                          activebackground='#A4C8E8')
    delete.image= photo
    delete.place(x=1790, y=890) 

#----------------  text Frame  -------------------------------
    textFrame =tk.Frame(dash ,bg='#A4C8E8')    
    textFrame.place(x=500, y=150, width=1400, height=300)
    
    textFrame =tk.Frame(dash ,bg='#A4C8E8')    
    textFrame.place(x=500, y=500, width=1400, height=300)

chk_frontend()

dash.mainloop()