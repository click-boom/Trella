import tkinter as tk
from PIL import ImageTk, Image
import sqlite3
from tkcalendar import Calendar, DateEntry
dash=tk.Tk()
dash.title('TRELLA')
dash.geometry('1920x1080')
dash.minsize(1920, 1080)

icon=tk.PhotoImage(file='D:/TRELLA/Images/llogo.png')
dash .iconphoto(True, icon)
#========================FRONT END======================================
#-------------------  Theme  -----------------------------
            
lth_clr='#A4C7EE'
dth_clr='#192436'
btn_bg='#104289'
frm_clr='#A4C8EB'

lfnt=lth_clr
dfnt=dth_clr

def ok():
    toggle_fr.destroy()
    rem_frame()

def dell_fr():
    for frame in iframe.winfo_children():
        frame.destroy()

def fetch_date():
        date_lbl.config(text=cal.get_date())
        print(cal.get_date())

    
def cal_toggle_open():
    global toggle_fr
    toggle_fr=tk.Frame(iframe, bg=dth_clr)
    toggle_fr.place(width=235, height=250, x=980 , y=690)
    

    global cal
    cal=DateEntry(toggle_fr, selectmode='day')
    cal.grid()

    get_btn=tk.Button(toggle_fr, text='Pick date',font=('yu gothic ui', 12, 'bold'), fg=lfnt, bg=btn_bg, bd=0, highlightthickness=0, command=fetch_date)
    get_btn.place(x=10, y=220)


    OK_btn=tk.Button(toggle_fr, text='OK',font=('yu gothic ui', 12, 'bold'), fg=lfnt, bg=btn_bg, bd=0, highlightthickness=0, command=ok)
    OK_btn.place(x=120, y=220)
    
    global date_lbl
    date_lbl=tk.Label(toggle_fr, text='', fg=lfnt, bg=dth_clr, font=('yu gothic ui', 12, 'bold' ))
    date_lbl.grid(row=1, pady=170)
    



#----------------------------------------------------------
def chk_frontend():
    

#--------------------  Inner Frame  -------------------------------
    global iframe
    iframe=tk.Frame(dash)
    iframe.place(x=400, y=0, width='1520', height='1080')
    
    # #------------------  Frame background  ---------------------------
        
    dashfr_img=ImageTk.PhotoImage(Image.open('D:/TRELLA/Images/dash_bg.png'))
    dash_bg=tk.Label(iframe, image=dashfr_img)
    dash_bg.image=dashfr_img
    dash_bg.pack(fill='both', expand='yes')

#------------------  Inner inner Frame  ---------------------------
    
    iiframe=tk.Frame(iframe, bg='white')
    iiframe.place(x=220, y=100, width='1038', height='800')
    
    iiframe_img=ImageTk.PhotoImage(Image.open('D:/TRELLA/Images/iiframe.png'))
    after_entry=tk.Label(iiframe, image=iiframe_img)
    after_entry.image=iiframe_img
    after_entry.pack(fill='both', expand='yes')

    
#------------------  SIDEBAR  ---------------------------
    sidebar =tk.Frame(dash ,bg=dth_clr)    
    sidebar.place(x=0, y=0, width=400, height=1100)
        
#----------------  Logo Frame  -------------------
    
    lframe =tk.Frame(sidebar ,bg=dth_clr)    
    lframe.place(x=50, y=50, width=300, height=250)

    #----------------  Logo Image -------------------
    
    dash_logo=ImageTk.PhotoImage(Image.open('D:/TRELLA/Images/llogo.png'))
    logo_lbl=tk.Label(lframe, image=dash_logo, bg= dth_clr)
    logo_lbl.image=dash_logo
    logo_lbl.pack(side='top') 
    
    #----------------  Logo Label -------------------

    logo_lbl=tk.Label(lframe, text='Hello Haseena', bg= dth_clr, font=('yu gothic ui', 25, 'bold'), fg=lfnt)
    logo_lbl.image=dash_logo
    logo_lbl.pack(side='bottom') 

# ====================  Button Labels  ========================
    #-----------------Checklist--------------------------
    btn_img=tk.PhotoImage(file='D:/TRELLA/Images/dash_btn.png')
    
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
    
    chk_img=ImageTk.PhotoImage(Image.open('D:/TRELLA/Images/check-list.png'))
    chk_img.image=chk_img
    chk_btn=tk.Button(chk_btn_lbl, text='          CHECKLIST',font=('yu gothic ui', 25, 'bold'), bg=btn_bg, fg=lfnt, cursor='hand2', activebackground=btn_bg,activeforeground='white', bd=0,highlightthickness=0 )
    chk_btn.place(x=30, y=7)

    chk_img_lbl=tk.Label(chk_btn, image=chk_img, bg=btn_bg)
    chk_img_lbl.place(x=10, y=10)
    
    #-----------------  reminder  --------------------------
    
    rem_img=ImageTk.PhotoImage(Image.open('D:/TRELLA/Images/reminder.png'))
    rem_img.image=rem_img
    rem_btn=tk.Button(rem_btn_lbl, text='          REMINDER',font=('yu gothic ui', 25, 'bold'), bg=btn_bg, fg='white', cursor='hand2', activebackground=btn_bg, activeforeground='white',bd=0,highlightthickness=0 )
    rem_btn.place(x=30, y=10)

    rem_img_lbl=tk.Label(rem_btn, image=rem_img, bg=btn_bg)
    rem_img_lbl.place(x=10, y=10)

    #-----------------  sticky notes --------------------------
    
    st_img=ImageTk.PhotoImage(Image.open('D:/TRELLA/Images/reminder.png'))
    st_img.image=st_img
    st_btn=tk.Button(st_btn_lbl, text='            NOTES',font=('yu gothic ui', 25, 'bold'), bg=btn_bg, fg=lfnt, cursor='hand2', activebackground=btn_bg,activeforeground='white', bd=0,highlightthickness=0 )
    st_btn.place(x=30, y=10)

    st_img_lbl=tk.Label(st_btn, image=st_img, bg=btn_bg)
    st_img_lbl.place(x=10, y=10)


#-----------------  Logout Button  --------------------------

    lcircle_img=tk.PhotoImage(file='D:/TRELLA/Images/l_btn.png')
    lcircle_img.image=lcircle_img
    lcircle_lbl=tk.Label(sidebar, image=lcircle_img, bg=dth_clr, bd=0)
    lcircle_lbl.place(x=135, y=670)

    lbtn_img=tk.PhotoImage(file='D:/TRELLA/Images/logout.png')
    lbtn_img.image=lbtn_img
    lbtn=tk.Button(lcircle_lbl, image=lbtn_img, bg=btn_bg, activebackground=btn_bg, cursor='hand2', highlightthickness=0, bd=0)
    lbtn.place(x=19, y=15)

def rem_frame():
#----------------  Dashboard Heading  -------------------
    heading =tk.Label(iframe , text='Sticky Notes',font=('yu gothic ui', 44, 'bold'),bg=dth_clr, fg=lfnt)
    heading.place(x=650, y=0)
        
    dashfr_img=ImageTk.PhotoImage(Image.open('D:/TRELLA/Images/dash_bg.png'))
    dash_bg=tk.Label(iframe, image=dashfr_img)
    dash_bg.image=dashfr_img
    dash_bg.pack(fill='both', expand='yes')
#===========================  Add Writing Area  ======================================   
    
    note= tk.Text(iframe, width=150, height=46, bg=dth_clr, fg=lfnt, insertbackground=lth_clr, bd=0, highlightthickness=0)
    note.place(x=240, y=120)
 
    down_frame=tk.Frame(iframe,width=1200,height=70,bg=dth_clr)
    down_frame.place(x=170,y=950)
# ...................plus-icon.........................
    plusicon= Image.open('D://TRELLA/Images/add.png')
    
    photo = ImageTk.PhotoImage(plusicon)
    plus=tk. Button(down_frame, 
                          image=photo,
                          bg='#ffffff',
                          bd=0,
                          cursor='hand2',
                          activebackground='#ffffff')
    plus.image= photo
    plus.place(x=50, y=20) 
    
# ...................A-icon.........................
    Aicon= Image.open('D://TRELLA/Images/A.png')
    
    photo = ImageTk.PhotoImage(Aicon)
    a=tk. Button(down_frame, 
                          image=photo,
                          bg='#ffffff',
                          bd=0,
                          cursor='hand2',
                          activebackground='#ffffff')
    a.image= photo
    a.place(x=220, y=20) 

# ...................attach-icon.........................

    attachicon= Image.open('D://TRELLA/Images/attach.png')
    photo = ImageTk.PhotoImage(attachicon)
    attach=tk. Button(down_frame, 
                          image=photo,
                          bg='#ffffff',
                          bd=0,
                          cursor='hand2',
                          activebackground='#ffffff')
    attach.image= photo
    attach.place(x=150, y=20) 
    
# ...................delete-icon.........................

    deleteicon= Image.open('D://TRELLA/Images/delete.png')
    photo = ImageTk.PhotoImage(deleteicon)
    delete=tk. Button(down_frame, 
                          image=photo,
                          bg='#ffffff',
                          bd=0,
                          cursor='hand2',
                          activebackground='#ffffff')
    delete.image= photo
    delete.place(x=1130, y=20) 

def fetch_rem_backend(user_data:str):
    conn =sqlite3.connect("reg_usrs.db")
    c=conn.cursor()
    
    c.execute("SELECT * FROM sticky_table WHERE belongs_to=?",user_data['ID'])
    print(c.fetchall())  

#------------------------date time_button _frame---------------------------


chk_frontend()
rem_frame()
dash.mainloop()