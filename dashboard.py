import tkinter as tk
from PIL import ImageTk, Image
from tkcalendar import Calendar
from datetime import datetime
from tktimepicker import AnalogPicker,AnalogThemes 
import sqlite3

dash=tk.Tk()
dash.title('TRELLA')
dash.geometry('1920x1080')
dash.minsize(1920, 1080)

icon=tk.PhotoImage(file='/home/wae/Documents/giri raj sir/Trella/Images/llogo.png')
dash .iconphoto(True, icon)

#========================  INDICATOR FUNCTION  ======================================

def dash_unindicate():
    chk_btn.config(fg=lfnt)
    rem_btn.config(fg=lfnt)
    st_btn.config(fg=lfnt)
    
def dash_indicate(ind, page):
    dash_unindicate()
    ind.config(fg='white')
    dell_fr()
    page()

def dell_fr():
    for frame in iframe.winfo_children():
        frame.destroy()

def fetch_date():
        real_date = datetime.strptime(cal.get_date(),"%m/%d/%y")
        global db_date
        db_date=str(real_date).split(" ")[0]
        date_lbl.config(text=db_date)

def fetch_time():
    time: tuple = time_picker.time()
    time_lbl.config(text=time)
    global time_value
    time_value=time

def fetch_and_push():
    new_entry=tk.Label(iiframe, bg='black', text=(add_entry.get()), width=1098, height=50)
    new_entry.grid()
    new_entry.rowconfigure(1, weight=1)

def on_press(str):
    add_entry.delete(0, tk.END)

def on_unpress(str):
    add_entry.delete(0, tk.END)
    if add_entry.get()=='':
        add_entry.insert(0,'Add Reminder')

def fetch_and_push(user_data):
    return
    # conn=sqlite3.connect("reg_usrs.db")
    # c=conn.cursor()
    
    # time=str(time_value[0]) + ':' + str(time_value[1]) + time_value[2]
    
    # c.execute("SELECT * FROM reminder_table WHERE username='Rohan'")
    # rows = c.fetchall()
    # for row in rows:
    #     print(row)

    # c.execute("INSERT INTO reminder_table(Description, Deploy_date, Deploy_time, is_repeat, belongs_to) VALUES (?, ?, ?, ?, ?)",[add_entry.get(), db_date, time, 1, user_data["ID"]])
    # conn.commit()
        # print(add_entry.get())
        # print(db_date)
        # hr=str(time_value[0])
        # min=str(time_value[1])
        # print(hr, end=':')
        # print(min, end=' ')
        # print(time_value[2])

def ok(frname):
    frname.destroy()
    
def cal_toggle_open():
    global cal_toggle_fr
    cal_toggle_fr=tk.Frame(iframe, bg=dth_clr)
    cal_toggle_fr.place(width=235, height=250, x=980 , y=690)
    

    global cal
    cal=Calendar(cal_toggle_fr, selectmode='day')
    cal.grid()

    get_btn=tk.Button(cal_toggle_fr, text='Pick date',font=('yu gothic ui', 12, 'bold'), fg=lfnt, bg=btn_bg, bd=0, highlightthickness=0, command=fetch_date)
    get_btn.place(x=10, y=220)


    OK_btn=tk.Button(cal_toggle_fr, text='OK',font=('yu gothic ui', 12, 'bold'), fg=lfnt, bg=btn_bg, bd=0, highlightthickness=0, command=lambda: ok(cal_toggle_fr))
    OK_btn.place(x=120, y=220)
    
    global date_lbl
    date_lbl=tk.Label(cal_toggle_fr, text='', fg=lfnt, bg=dth_clr, font=('yu gothic ui', 12, 'bold'))
    date_lbl.place(x=10, y=180)
    
def timepick():
    al_toggle_fr=tk.Frame(iframe, bg=dth_clr , width=400, height=400)
    al_toggle_fr.place( x=1050 , y=530)

    cl_toggle_fr=tk.Frame(al_toggle_fr, bg='white')
    cl_toggle_fr.place( x=10, y=10)
    
    global time_picker
    time_picker = AnalogPicker(cl_toggle_fr)
    time_picker.pack(expand=True, fill='both')

    theme = AnalogThemes(time_picker)
    theme.setDracula()

    OKay_btn=tk.Button(al_toggle_fr, text='OK',font=('yu gothic ui', 12, 'bold'),fg=lfnt, bg=btn_bg,bd=0,highlightthickness=0, command=lambda: ok(al_toggle_fr))
    OKay_btn.place(x=130, y=350, width=70)

    get_btn=tk.Button(al_toggle_fr, text='Pick Time',
    font=('yu gothic ui', 12, 'bold'),
    fg=lfnt, 
    bg=btn_bg,
    bd=0, 
    highlightthickness=0,
    command=fetch_time)
    get_btn.place(x=20, y=350)
    
    global time_lbl
    time_lbl=tk.Label(al_toggle_fr, text='', fg=lfnt, bg=dth_clr, font=('yu gothic ui', 12, 'bold'))
    time_lbl.place(x=295, y=350)

def logout():
        global sure_dialog
        sure_dialog=tk.Frame(sidebar, width=350, height=200, bg=dialog_bg, borderwidth=2)    
        sure_dialog.place(x=25, y=650)

        sure_lbl=tk.Label(sure_dialog, text='Are you sure you want to logout?',font=('yu gothic ui', 14, 'bold'), bg=dialog_bg, fg=lfnt)
        sure_lbl.place(x=40, y=70)

        Y_button= tk.Button(sure_dialog, text='Yes',
                                          font=('yu gothic ui', 12, 'bold'),
                                          fg=lfnt, 
                                          bg=btn_bg,
                                          bd=0, 
                                        highlightthickness=0, command=logout_yes)
        Y_button.place(x=105, y=125)

        N_button= tk.Button(sure_dialog, text='No',
                                          font=('yu gothic ui', 12, 'bold'),
                                          fg=lfnt, 
                                          bg=btn_bg,
                                          bd=0, 
                                        highlightthickness=0, command=logout_no)
        N_button.place(x=205, y=125)

def logout_yes():
    dash.destroy()
    import login

def logout_no():
    sure_dialog.destroy()
#=======================  FRONT END  ======================================
#------------------  Theme  -----------------------------
        
lth_clr='#A4C7EE'
dth_clr='#192436'
btn_bg='#104289'
frm_clr='#A4C8EB'
lfnt=lth_clr
dfnt=dth_clr
dialog_bg='#576B8B'

#----------------------------------------------------------
def chk_frontend(user_data:dict):
    dashfr=tk.Frame(dash, width=1230, height=746)
    dashfr.place(x=535, y=300)
#----------------------------------------  Inner Frame  -------------------------------------------------------------
    global iframe
    iframe=tk.Frame(dash)
    iframe.place(x=400, y=0, width='1520', height='1080')
    
#------------------  SIDEBAR  ---------------------------
    global sidebar
    sidebar =tk.Frame(dash ,bg=dth_clr)    
    sidebar.place(x=0, y=0, width=400, height=1100)
#----------------  Logo Frame  -------------------
    
    lframe =tk.Frame(sidebar ,bg=dth_clr)    
    lframe.place(x=50, y=50, width=300, height=250)

    #----------------  Logo Image -------------------
    
    dash_logo=ImageTk.PhotoImage(Image.open('/home/wae/Documents/giri raj sir/Trella/Images/llogo.png'))
    logo_lbl=tk.Label(lframe, image=dash_logo, bg= dth_clr)
    logo_lbl.image=dash_logo
    logo_lbl.pack(side='top') 
    
    #----------------  Logo Label -------------------

    logo_lbl=tk.Label(lframe, text='Hello '+user_data["username"], bg= dth_clr, font=('yu gothic ui', 25, 'bold'), fg=lfnt)
    logo_lbl.image=dash_logo
    logo_lbl.pack(side='bottom') 

# ====================  Button Labels  =======================================================================
    #-----------------Checklist--------------------------
    btn_img=tk.PhotoImage(file='/home/wae/Documents/giri raj sir/Trella1/Img/dash_btn.png')
        
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

 #=========================================================================================================================================================   
    

# ====================  Buttons  ================================================================================
    #-----------------  Checklist  --------------------------
    chk_img=ImageTk.PhotoImage(Image.open('/home/wae/Documents/giri raj sir/Trella/Images/check-list.png'))
    global chk_btn
    chk_btn=tk.Button(chk_btn_lbl, text='          CHECKLIST',font=('yu gothic ui', 25, 'bold'), bg=btn_bg, fg=lfnt, cursor='hand2', bd=0,highlightthickness=0, activebackground=btn_bg, activeforeground='white', command=lambda:dash_indicate(chk_btn, chk_frame))
    chk_btn.place(x=30, y=7)

    chk_img_lbl=tk.Label(chk_btn, image=chk_img, bg=btn_bg)
    chk_img_lbl.image=chk_img
    chk_img_lbl.place(x=10, y=10)
    
    #-----------------  reminder  --------------------------
    
    rem_img=ImageTk.PhotoImage(Image.open('/home/wae/Documents/giri raj sir/Trella/Images/reminder.png'))
    global rem_btn
    rem_btn=tk.Button(rem_btn_lbl, text='          REMINDER',font=('yu gothic ui', 25, 'bold'), bg=btn_bg, fg=lfnt, cursor='hand2', activebackground=btn_bg, activeforeground='white', bd=0,highlightthickness=0, command=lambda:dash_indicate(rem_btn,  rem_frame) )
    rem_btn.place(x=30, y=10)

    rem_img_lbl=tk.Label(rem_btn, image=rem_img, bg=btn_bg)
    rem_img_lbl.image=rem_img
    rem_img_lbl.place(x=10, y=10)

    #-----------------  sticky notes --------------------------
    
    st_img=ImageTk.PhotoImage(Image.open('/home/wae/Documents/giri raj sir/Trella/Images/sticky-note.png'))
    global st_btn
    st_btn=tk.Button(st_btn_lbl, text='       STICKY NOTES',font=('yu gothic ui', 25, 'bold'), bg=btn_bg, fg=lfnt, cursor='hand2', activebackground=btn_bg,activeforeground='white' , bd=0,highlightthickness=0, command=lambda:dash_indicate(st_btn, st_frame) )
    st_btn.place(x=30, y=10)

    st_img_lbl=tk.Label(st_btn, image=st_img, bg=btn_bg)
    st_img_lbl.image=st_img
    st_img_lbl.place(x=10, y=10)

#-----------------  Logout Button  --------------------------

    lcircle_img=tk.PhotoImage(file='/home/wae/Documents/giri raj sir/Trella/Images/l_btn.png')
    lcircle_lbl=tk.Label(sidebar, image=lcircle_img, bg=dth_clr, bd=0)
    lcircle_lbl.image=lcircle_img
    lcircle_lbl.place(x=135, y=670)

    lbtn_img=tk.PhotoImage(file='/home/wae/Documents/giri raj sir/Trella/Images/logout.png')
    lbtn=tk.Button(lcircle_lbl, image=lbtn_img, bg=btn_bg, activebackground=btn_bg, cursor='hand2', highlightthickness=0, bd=0, command=logout)
    lbtn.image=lbtn_img
    lbtn.place(x=19, y=15)

    
def rem_frame():

    dashfr_img=ImageTk.PhotoImage(Image.open('/home/wae/Documents/giri raj sir/Trella/Images/dash_bg.png'))
    dash_bg=tk.Label(iframe, image=dashfr_img)
    dash_bg.image=dashfr_img
    dash_bg.pack(fill='both', expand='yes')
    #------------------  Inner inner Frame  ---------------------------
    global iiframe
    iiframe=tk.Frame(iframe, bg='white')
    iiframe.place(x=220, y=100, width='1038', height='800')
    iiframe_img=ImageTk.PhotoImage(Image.open('/home/wae/Documents/giri raj sir/Trella/Images/iiframe.png'))
    after_entry=tk.Label(iiframe, image=iiframe_img)
    after_entry.image=iiframe_img
    after_entry.pack(fill='both', expand='yes')
    #--------------  Reminder Adding Section  --------------------- 
    down_frame=tk.Frame(iframe,width=1400,height=70,bg=dth_clr)
    down_frame.place(x=60,y=950)
    
# ----------------  Dashboard Heading  -------------------
    heading =tk.Label(iframe , text='Reminder',font=('yu gothic ui', 44, 'bold'),bg=dth_clr, fg=lfnt)
    heading.place(x=650, y=0)
    
#===========================  Calendar icon  ======================================
    calendar_icon=tk.PhotoImage(file='/home/wae/Documents/giri raj sir/Trella/Images/calendar.png')
    calendar_icon_lbl=tk.Button(down_frame,image=calendar_icon, bg=dth_clr, activebackground=dth_clr, activeforeground=dth_clr, highlightthickness=0, bd=0, cursor='hand2', command=cal_toggle_open)
    calendar_icon_lbl.image=calendar_icon
    calendar_icon_lbl.place(x=1210,y=20)
#===========================  Alarm icon  ======================================
    alarm_icon=tk.PhotoImage(file='/home/wae/Documents/giri raj sir/Trella1/Img/alarm.png')
    alarm_icon_lbl=tk.Button(down_frame,image=alarm_icon, bg=dth_clr, activebackground=dth_clr, activeforeground=dth_clr, highlightthickness=0, bd=0, cursor='hand2', command=timepick )
    alarm_icon_lbl.image=alarm_icon
    alarm_icon_lbl.place(x=1270,y=17)
#===========================  Repeat icon  ======================================
    repeat_icon=tk.PhotoImage(file='/home/wae/Documents/giri raj sir/Trella1/Img/repeat.png')
    repeat_icon_lbl=tk.Button(down_frame,image=repeat_icon, bg=dth_clr, activebackground=dth_clr, activeforeground=dth_clr, highlightthickness=0, bd=0, cursor='hand2' )
    repeat_icon_lbl.image=repeat_icon
    repeat_icon_lbl.place(x=1330,y=20)

#===========================  Add Writing Area  ======================================

    entry_var=tk.StringVar()
    global add_entry
    add_entry=tk.Entry(down_frame, font=('yu gothic ui', 20, 'bold'), fg=lth_clr, bg=dth_clr, bd=0 ,highlightthickness=0, textvariable=entry_var, insertbackground=lth_clr, width=60)
    add_entry.place(x=70,y=15)
    add_entry.insert(0,'Add Reminder....')
    add_entry.bind("<FocusIn>",on_press)
    add_entry.bind("<FocusOut>",on_unpress)

    
    add_button=tk.PhotoImage(file='/home/wae/Documents/giri raj sir/Trella1/Img/add.png')
    add_button_lbl=tk.Button(down_frame,image=add_button,bg=dth_clr,activebackground=dth_clr,activeforeground=dth_clr, highlightthickness=0, bd=0, cursor='hand2', command=fetch_and_push)
    add_button_lbl.image=add_button
    add_button_lbl.place(x=16,y=16)
        

def st_frame():
#----------------  Dashboard Heading  -------------------
    heading =tk.Label(iframe , text='Sticky Notes',font=('yu gothic ui', 44, 'bold'),bg=dth_clr, fg=lfnt)
    heading.place(x=650, y=0)
        
    dashfr_img=ImageTk.PhotoImage(Image.open('/home/wae/Documents/giri raj sir/Trella/Images/dash_bg.png'))
    dash_bg=tk.Label(iframe, image=dashfr_img)
    dash_bg.image=dashfr_img
    dash_bg.pack(fill='both', expand='yes')
#===========================  Add Writing Area  ======================================   
    
    note= tk.Text(iframe, width=150, height=46, bg=dth_clr, fg=lfnt, insertbackground=lth_clr, bd=0, highlightthickness=0)
    note.place(x=240, y=120)
 
    down_frame=tk.Frame(iframe,width=1200,height=70,bg=dth_clr)
    down_frame.place(x=170,y=950)

def chk_frame():
    return
    
if __name__=="__main__":
    chk_frontend()

def run_dashboard(user_data:dict):
    chk_frontend(user_data)
    dash.mainloop()
