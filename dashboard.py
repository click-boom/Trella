import tkinter as tk
from PIL import ImageTk, Image

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
    
#========================  FRONT END  ======================================
#-------------------  Theme  -----------------------------
            
lth_clr='#A4C7EE'
dth_clr='#192436'
btn_bg='#104289'
frm_clr='#A4C8EB'

lfnt=lth_clr
dfnt=dth_clr

#----------------------------------------------------------
def chk_frontend(user_data:dict):
    dashfr=tk.Frame(dash, width=1230, height=746)
    dashfr.place(x=535, y=300)
#----------------------------------------  Inner Frame  -------------------------------------------------------------
    global iframe
    iframe=tk.Frame(dash)
    iframe.place(x=400, y=0, width='1520', height='1080')
    
#------------------  SIDEBAR  ---------------------------
    sidebar =tk.Frame(dash ,bg=dth_clr)    
    sidebar.place(x=0, y=0, width=400, height=1100)
#----------------  Dashboard Heading  -------------------
    # heading =tk.Label(dash , text='Dashboard',font=('yu gothic ui', 44, 'bold'),bg=dth_clr, fg=lfnt)
    # heading.place(x=950, y=35)
        
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
    chk_img.image=chk_img
    global chk_btn
    chk_btn=tk.Button(chk_btn_lbl, text='          CHECKLIST',font=('yu gothic ui', 25, 'bold'), bg=btn_bg, fg=lfnt, cursor='hand2', bd=0,highlightthickness=0, activebackground=btn_bg, activeforeground='white', command=lambda:dash_indicate(chk_btn))
    chk_btn.place(x=30, y=7)

    chk_img_lbl=tk.Label(chk_btn, image=chk_img, bg=btn_bg)
    chk_img_lbl.place(x=10, y=10)
    
    #-----------------  reminder  --------------------------
    
    rem_img=ImageTk.PhotoImage(Image.open('/home/wae/Documents/giri raj sir/Trella/Images/reminder.png'))
    rem_img.image=rem_img
    global rem_btn
    rem_btn=tk.Button(rem_btn_lbl, text='          REMINDER',font=('yu gothic ui', 25, 'bold'), bg=btn_bg, fg=lfnt, cursor='hand2', activebackground=btn_bg, activeforeground='white', bd=0,highlightthickness=0, command=lambda:dash_indicate(rem_btn,  rem_frame) )
    rem_btn.place(x=30, y=10)

    rem_img_lbl=tk.Label(rem_btn, image=rem_img, bg=btn_bg)
    rem_img_lbl.place(x=10, y=10)

    #-----------------  sticky notes --------------------------
    
    st_img=ImageTk.PhotoImage(Image.open('/home/wae/Documents/giri raj sir/Trella/Images/sticky-note.png'))
    st_img.image=st_img
    global st_btn
    st_btn=tk.Button(st_btn_lbl, text='       STICKY NOTES',font=('yu gothic ui', 25, 'bold'), bg=btn_bg, fg=lfnt, cursor='hand2', activebackground=btn_bg,activeforeground='white' , bd=0,highlightthickness=0, command=lambda:dash_indicate(st_btn, st_page) )
    st_btn.place(x=30, y=10)

    st_img_lbl=tk.Label(st_btn, image=st_img, bg=btn_bg)
    st_img_lbl.place(x=10, y=10)

#-----------------  Logout Button  --------------------------

    lcircle_img=tk.PhotoImage(file='/home/wae/Documents/giri raj sir/Trella/Images/l_btn.png')
    lcircle_img.image=lcircle_img
    lcircle_lbl=tk.Label(sidebar, image=lcircle_img, bg=dth_clr)
    lcircle_lbl.place(x=145, y=660)

    lbtn_img=tk.PhotoImage(file='/home/wae/Documents/giri raj sir/Trella/Images/logout.png')
    lbtn_img.image=lbtn_img
    lbtn=tk.Button(lcircle_lbl, image=lbtn_img, bg=btn_bg, activebackground=btn_bg, cursor='hand2', highlightthickness=0, bd=0)
    lbtn.place(x=19, y=15)

    
def rem_frame():

    dashfr_img=ImageTk.PhotoImage(Image.open('/home/wae/Documents/giri raj sir/Trella/Images/dash_bg.png'))
    dash_bg=tk.Label(iframe, image=dashfr_img)
    dash_bg.image=dashfr_img
    dash_bg.pack(fill='both', expand='yes')
    #------------------  Inner inner Frame  ---------------------------

    iiframe=tk.Frame(iframe, bg='white')
    iiframe.place(x=220, y=100, width='1038', height='800')
    iiframe_img=ImageTk.PhotoImage(Image.open('/home/wae/Documents/giri raj sir/Trella/Images/iiframe.png'))
    after_entry=tk.Label(iiframe, image=iiframe_img)
    after_entry.image=iiframe_img
    after_entry.pack(fill='both', expand='yes')
    #--------------  Reminder Adding Section  --------------------- 
    down_frame=tk.Frame(iframe,width=1400,height=70,bg=dth_clr)
    down_frame.place(x=60,y=950)
    
#===========================  Calendar icon  ======================================
    calendar_icon=tk.PhotoImage(file='/home/wae/Documents/giri raj sir/Trella/Images/calendar.png')
    calendar_icon.image=calendar_icon
    calendar_icon_lbl=tk.Button(down_frame,image=calendar_icon, bg=dth_clr, activebackground=dth_clr, activeforeground=dth_clr, highlightthickness=0, bd=0, cursor='hand2' )
    calendar_icon_lbl.place(x=1210,y=20)
#===========================  Alarm icon  ======================================
    alarm_icon=tk.PhotoImage(file='/home/wae/Documents/giri raj sir/Trella1/Img/alarm.png')
    alarm_icon.image=alarm_icon
    alarm_icon_lbl=tk.Button(down_frame,image=alarm_icon, bg=dth_clr, activebackground=dth_clr, activeforeground=dth_clr, highlightthickness=0, bd=0, cursor='hand2' )
    alarm_icon_lbl.place(x=1270,y=17)
#===========================  Repeat icon  ======================================
    repeat_icon=tk.PhotoImage(file='/home/wae/Documents/giri raj sir/Trella1/Img/repeat.png')
    repeat_icon.image=repeat_icon
    repeat_icon_lbl=tk.Button(down_frame,image=repeat_icon, bg=dth_clr, activebackground=dth_clr, activeforeground=dth_clr, highlightthickness=0, bd=0, cursor='hand2' )
    repeat_icon_lbl.place(x=1330,y=20)

#===========================  Add Writing Area  ======================================

    entry_var=tk.StringVar(value='Add reminders...')
    down_frame_entry=tk.Entry(down_frame, font=('yu gothic ui', 20, 'bold'), fg=lth_clr, bg=dth_clr, bd=0 ,highlightthickness=0, textvariable=entry_var, insertbackground=lth_clr)
    down_frame_entry.place(x=65,y=15)
    add_button=tk.PhotoImage(file='/home/wae/Documents/giri raj sir/Trella1/Img/add.png')
    add_button.image=add_button
    add_button_lbl=tk.Button(down_frame,image=add_button,bg=dth_clr,activebackground=dth_clr,activeforeground=dth_clr, highlightthickness=0, bd=0, cursor='hand2')
    add_button_lbl.place(x=16,y=16)


def st_page():
    dashfr_img=ImageTk.PhotoImage(Image.open('/home/wae/Documents/giri raj sir/Trella/Images/dash_bg.png'))
    dash_bg=tk.Label(iframe, image=dashfr_img)
    dash_bg.image=dashfr_img
    dash_bg.pack(fill='both', expand='yes')
#===========================  Add Writing Area  ======================================   
    
    note= tk.Text(iframe, width=150, height=46, bg=dth_clr, insertbackground=lth_clr, bd=0, highlightthickness=0)
    note.place(x=240, y=120)
 
    down_frame=tk.Frame(iframe,width=1200,height=70,bg=dth_clr)
    down_frame.place(x=170,y=950)

if __name__=="__main__":
    chk_frontend()

def run_dashboard(user_data:dict):
    chk_frontend(user_data)
    dash.mainloop()