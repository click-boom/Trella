import tkinter as tk
from tkinter import ttk,messagebox
from PIL import ImageTk, Image
from tkcalendar import Calendar
from datetime import datetime
from tktimepicker import AnalogPicker,AnalogThemes 
import sqlite3
from playsound import playsound
import notify2

import multiprocessing
dash=tk.Tk()
dash.title('TRELLA')
dash.geometry('1920x1080')
dash.minsize(1920, 1080)

icon=tk.PhotoImage(file='/home/rolen/Downloads/11/Images/llogo.png')
dash .iconphoto(True, icon)
#========================  INDICATOR FUNCTION  ======================================
def dash_unindicate():
    chk_btn.config(fg=lfnt)
    rem_btn.config(fg=lfnt)
    st_btn.config(fg=lfnt)
    
def dash_indicate(ind, page):
    dash_unindicate()
    ind.config(fg='white')
    dell_for_change_fr()
    page()

def dell_for_change_fr():
    for frame in iframe.winfo_children():
        frame.destroy()

def on_rem_title_press(str):
    add_title.delete(0, tk.END)

def on_rem_title_unpress(str):
    add_title.delete(0, tk.END)
    if add_title.get()=='':
        add_title.insert(0,'Reminder Title...')

def on_rem_description_press(str):
    add_description.delete(0, tk.END)

def on_rem_description_unpress(str):
    add_description.delete(0, tk.END)
    if add_description.get()=='':
        add_description.insert(0,'Reminder Description...')

def ok(frname):
    frname.destroy()
    try:
        view_fr.destroy()
    except:
        pass

def tree():
        tree_fnt=15
        global tree_scroll_frame
        tree_scroll_frame=ttk.Treeview(iframe)
        tree_scroll_frame['show']='headings'
        tree_scroll_frame.place(relx=0.15,rely=0.1,width=1038,height=750)
        ttk.Style().configure("Treeview", font=('yu gothic ui', tree_fnt, 'bold'),background=dth_clr, foreground=lfnt, fieldbackground=dth_clr, rowheight=int(tree_fnt*2.5))
        ttk.Style().configure("Treeview.Heading", font=('yu gothic ui', 20, 'bold'), background=dialog_bg, foreground=lth_clr)

        scrollbarX=tk.Scrollbar(iframe,orient=tk.HORIZONTAL, background=lth_clr, activebackground=lth_clr, troughcolor=dth_clr)
        scrollbarX.place(relx=0.15,rely=0.7970,height=12,width=1040)
        
        scrollbarY=tk.Scrollbar(iframe,orient=tk.VERTICAL, background=lth_clr, activebackground=lth_clr, troughcolor=dth_clr)
        scrollbarY.place(relx=0.8325,rely=0.0995,width=12,height=750)
        
        tree_scroll_frame.configure(xscrollcommand=scrollbarX.set,yscrollcommand=scrollbarY.set)
        tree_scroll_frame.configure(selectmode=tk.EXTENDED)

        scrollbarY.configure(command=tree_scroll_frame.yview)
        scrollbarX.configure(command=tree_scroll_frame.xview)
        tree_scroll_frame.configure(
            columns=('ID','Title','Description','Deploy date', 'Deploy time', 'Repeat')

        )
        tree_scroll_frame.heading("#0",text="S.N",anchor=tk.W)
        tree_scroll_frame.heading("ID",text="ID",anchor=tk.W)
        tree_scroll_frame.heading("Title",text="Title",anchor=tk.W)
        tree_scroll_frame.heading("Description",text="Description",anchor=tk.W)
        tree_scroll_frame.heading("Deploy date",text="Deploy date",anchor=tk.W)
        tree_scroll_frame.heading("Deploy time",text="Deploy time",anchor=tk.W)
        tree_scroll_frame.heading("Repeat",text="Repeat",anchor=tk.W)



        tree_scroll_frame.column("#0",width=120,minwidth=40)
        tree_scroll_frame.column("ID",width=120,minwidth=20)
        tree_scroll_frame.column("Title",width=120,minwidth=20)
        tree_scroll_frame.column("Description",width=120,minwidth=55)
        tree_scroll_frame.column("Deploy date",width=120,minwidth=45)
        tree_scroll_frame.column("Deploy time",width=120,minwidth=55)
        tree_scroll_frame.column("Repeat",width=120,minwidth=40)

def view_in_tree_data(user_id):
    conn=sqlite3.connect('reg_usrs.db')
    c=conn.cursor()

    c.execute("SELECT * FROM reminder_table WHERE belongs_to=(?)", [user_id])
    i=0
    for val in c:
        tree_scroll_frame.insert("", i, text=i+1, values=(val[0], val[1], val[2], val[3], val[4], val[5]))
        i+=1
    
def view_data_btn():
    iiframe.destroy()
    tree()
    view_in_tree_data(uid)


def logout():
        global sure_dialog
        sure_dialog=tk.Frame(sidebar, width=350, height=200, bg=dialog_bg, borderwidth=2)    
        sure_dialog.place(x=25, y=650)

        sure_lbl=tk.Label(sure_dialog, text='Are you sure you want to logout?',font=('yu gothic ui', 14, 'bold'), bg=dialog_bg, fg=lfnt)
        sure_lbl.place(x=40, y=70)

        Y_button= tk.Button(sure_dialog, text='Yes', font=('yu gothic ui', 12, 'bold'), fg=lfnt, bg=btn_bg, bd=0, highlightthickness=0, command=logout_yes)
        Y_button.place(x=105, y=125)

        N_button= tk.Button(sure_dialog, text='No',font=('yu gothic ui', 12, 'bold'),fg=lfnt, bg=btn_bg,bd=0, highlightthickness=0, command=logout_no)
        N_button.place(x=205, y=125)

def logout_yes():
    dash.destroy()
    import login

def logout_no():
    sure_dialog.destroy()
    
def add_frame():
        dell_for_change_fr()
        try:
            toplvl.destroy()
        except:
            pass
        rem_frame()

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
    
    dashfr_img=ImageTk.PhotoImage(Image.open('/home/rolen/Downloads/11/Images/dash_bg.png'))
    dash_bg=tk.Label(iframe, image=dashfr_img)
    dash_bg.image=dashfr_img
    dash_bg.pack(fill='both', expand='yes')
#------------------    ---------------------------
    heading =tk.Label(iframe , text='Welcome To TRELLA',font=('yu gothic ui', 50, 'bold'),bg=dth_clr, fg=lfnt)
    heading.place(x=500, y=0)
    
    intro = "Please Choose the options \nfrom the navigation Panel \nto Access the widgets"
    label = tk.Text(iframe, width=23, height=5, borderwidth=0, font=('yu gothic ui', 49, 'bold'), highlightthickness=0, bd=0, bg=dth_clr, fg=lfnt)
    label.insert("1.0", intro)
    label.config(state="disabled")

    label.place(x=280, y=300)
#------------------  SIDEBAR  ---------------------------
    global sidebar
    sidebar =tk.Frame(dash ,bg=dth_clr)    
    sidebar.place(x=0, y=0, width=400, height=1100)
#----------------  Logo Frame  -------------------
    
    lframe =tk.Frame(sidebar ,bg=dth_clr)    
    lframe.place(x=50, y=50, width=300, height=250)

    #----------------  Logo Image -------------------
    
    dash_logo=ImageTk.PhotoImage(Image.open('/home/rolen/Downloads/11/Images/llogo.png'))
    logo_lbl=tk.Label(lframe, image=dash_logo, bg= dth_clr)
    logo_lbl.image=dash_logo
    logo_lbl.pack(side='top') 
    
    #----------------  Logo Label -------------------

    logo_lbl=tk.Label(lframe, text='Hello '+user_data["username"], bg= dth_clr, font=('yu gothic ui', 25, 'bold'), fg=lfnt)
    logo_lbl.image=dash_logo
    logo_lbl.pack(side='bottom') 

# ====================  Button Labels  =======================================================================
    #-----------------Checklist--------------------------
    btn_img=tk.PhotoImage(file='/home/rolen/Downloads/11/Images/dash_btn.png')
        
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

 #=========================================================================================================================================
# ====================  Buttons  ================================================================================
    #-----------------  Checklist  --------------------------
    chk_img=ImageTk.PhotoImage(Image.open('/home/rolen/Downloads/11/Images/check-list.png'))
    global chk_btn
    chk_btn=tk.Button(chk_btn_lbl, text='          CHECKLIST',font=('yu gothic ui', 25, 'bold'), bg=btn_bg, fg=lfnt, cursor='hand2', bd=0,highlightthickness=0, activebackground=btn_bg, activeforeground='white', command=lambda:dash_indicate(chk_btn, chk_frame))
    chk_btn.place(x=30, y=7)

    chk_img_lbl=tk.Label(chk_btn, image=chk_img, bg=btn_bg)
    chk_img_lbl.image=chk_img
    chk_img_lbl.place(x=10, y=10)
    
    #-----------------  reminder  --------------------------
    
    rem_img=ImageTk.PhotoImage(Image.open('/home/rolen/Downloads/11/Images/reminder.png'))
    global rem_btn
    rem_btn=tk.Button(rem_btn_lbl, text='          REMINDER',font=('yu gothic ui', 25, 'bold'), bg=btn_bg, fg=lfnt, cursor='hand2', activebackground=btn_bg, activeforeground='white', bd=0,highlightthickness=0, command=lambda:dash_indicate(rem_btn,  rem_frame) )
    rem_btn.place(x=30, y=10)

    rem_img_lbl=tk.Label(rem_btn, image=rem_img, bg=btn_bg)
    rem_img_lbl.image=rem_img
    rem_img_lbl.place(x=10, y=10)

    #-----------------  sticky notes --------------------------
    
    st_img=ImageTk.PhotoImage(Image.open('/home/rolen/Downloads/11/Images/sticky-note.png'))
    global st_btn
    st_btn=tk.Button(st_btn_lbl, text='       STICKY NOTES',font=('yu gothic ui', 25, 'bold'), bg=btn_bg, fg=lfnt, cursor='hand2', activebackground=btn_bg,activeforeground='white' , bd=0,highlightthickness=0, command=lambda:dash_indicate(st_btn, note_frame) )
    st_btn.place(x=30, y=10)

    st_img_lbl=tk.Label(st_btn, image=st_img, bg=btn_bg)
    st_img_lbl.image=st_img
    st_img_lbl.place(x=10, y=10)

#-----------------  Logout Button  --------------------------

    lcircle_img=tk.PhotoImage(file='/home/rolen/Downloads/11/Images/l_btn.png')
    lcircle_lbl=tk.Label(sidebar, image=lcircle_img, bg=dth_clr, bd=0)
    lcircle_lbl.image=lcircle_img
    lcircle_lbl.place(x=135, y=670)

    lbtn_img=tk.PhotoImage(file='/home/rolen/Downloads/11/Images/logout.png')
    lbtn=tk.Button(lcircle_lbl, image=lbtn_img, bg=btn_bg, activebackground=btn_bg, cursor='hand2', highlightthickness=0, bd=0, command=logout)
    lbtn.image=lbtn_img
    lbtn.place(x=19, y=15)

    global uid
    uid=user_data['user_id']

def rem_frame():
    def cal_toggle_open():
        global cal_toggle_frame
        cal_toggle_frame=tk.Frame(iframe, bg=dth_clr)
        cal_toggle_frame.place(width=235, height=250, x=980 , y=690)

        global cal
        cal=Calendar(cal_toggle_frame, selectmode='day')
        cal.grid()

        get_btn=tk.Button(cal_toggle_frame, text='Pick date',font=('yu gothic ui', 12, 'bold'), fg=lfnt, bg=btn_bg, bd=0, highlightthickness=0, command=fetch_date)
        get_btn.place(x=10, y=220)


        OK_btn=tk.Button(cal_toggle_frame, text='OK',font=('yu gothic ui', 12, 'bold'), fg=lfnt, bg=btn_bg, bd=0, highlightthickness=0, command=lambda: ok(cal_toggle_frame))
        OK_btn.place(x=120, y=220)

        global date_lbl
        date_lbl=tk.Label(cal_toggle_frame, text='', fg=lfnt, bg=dth_clr, font=('yu gothic ui', 12, 'bold'))
        date_lbl.place(x=10, y=180)

    def recently_added_checklist():
        items=add_title.get()+(' '*10) +add_description.get()+(' '*10) +db_date+(' '*10)+time12
        new_entry.config(text=items)
        
        def convert_time():
            hours, minutes, meridian =time[0], time[1], time[2]
            hours = int(hours)

            if meridian == "PM" and hours != 12:
                hours += 12
        
            if meridian == "AM" and hours == 12:
                hours = 0
    
            return db_date+' '+"{:02d}:{:02d}:{}".format(hours, int(minutes),'00')    
        global dt
        dt = datetime.strptime(convert_time(), '%Y-%m-%d %H:%M:%S')
    
    def insert_into_reminder():
        conn=sqlite3.connect('reg_usrs.db')
        c=conn.cursor()
        try:
            c.execute("INSERT INTO reminder_table (title, description, deploy_date, deploy_time, date_time, is_repeat, belongs_to) VALUES (?, ?, ?, ?, ?, ?, ?)",[add_title.get(),add_description.get(), db_date, time12, dt, 0 , uid])
            conn.commit()
        except:
            pass
            
    
    def delete_from_reminder():
        val=tlevel_entry.get()
        conn=sqlite3.connect('reg_usrs.db')
        c=conn.cursor()

        try:
            c = conn.cursor()
            c.execute("DELETE FROM reminder_table WHERE ID=(?)",[val])
            conn.commit()
        
        except:
            pass
        view_data_btn()
    
    def reminder_lvl():
        iiframe.destroy()
        view_data_btn()
        global toplvl
        toplvl=tk.Toplevel()
        toplvl.geometry('400x150')
        toplvl.title('Delete Reminder')
        toplvl.config(bg=dth_clr)
        dialog_lbl=tk.Label(toplvl,text="Enter the reminder No. you want to delete", bg=dth_clr, fg=lfnt,font=('yu gothic ui', 12, 'bold'), pady=15)
        dialog_lbl.pack()
    
        global tlevel_entry
        tlevel_entry=tk.Entry(toplvl,width=23,font="Arial, 12")
        tlevel_entry.pack()

        del_btn=tk.Button(toplvl,text='DELETE',bg=dth_clr, fg=lfnt, font=('yu gothic ui', 12, 'bold') ,command=delete_from_reminder)
        del_btn.place(x=250,y=100)

        close_btn=tk.Button(toplvl,text='OK',font=('yu gothic ui', 12, 'bold'), bg=dth_clr, fg=lfnt, command=tree_ok)
        close_btn.place(x=340,y=100)

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
    
    def fetch_date():
        real_date = datetime.strptime(cal.get_date(),"%m/%d/%y")
        global db_date
        db_date=str(real_date).split(" ")[0]
        date_lbl.config(text=db_date)

    def fetch_time():
        global time
        time= time_picker.time()
        time_lbl.config(text=time)
        global time12
        time12=str(time[0])+':'+str(time[1])+' '+time[2]

    def tree_ok():
        toplvl.destroy()
        view_data_btn()
    
    dashfr_img=ImageTk.PhotoImage(Image.open('/home/rolen/Downloads/11/Images/dash_bg.png'))
    dash_bg=tk.Label(iframe, image=dashfr_img)
    dash_bg.image=dashfr_img
    dash_bg.pack(fill='both', expand='yes')

    Add_btn=tk.Button(iframe,text='Add to Reminders', bg=dth_clr, fg=lfnt , font=('yu gothic ui', 20, 'bold'), activebackground=dth_clr, activeforeground='white', highlightthickness=0, bd=0, cursor='hand2', command=insert_into_reminder)
    Add_btn.place(x=1010, y=620)
    
    Delete_btn=tk.Button(iframe,text='Delete Reminders', bg=dth_clr, fg=lfnt , font=('yu gothic ui', 20, 'bold'), activebackground=dth_clr, activeforeground='white', highlightthickness=0, bd=0, cursor='hand2', command=reminder_lvl )
    Delete_btn.place(x=280, y=900)
    
    View_btn=tk.Button(iframe,text='View Reminders', bg=dth_clr, fg=lfnt , font=('yu gothic ui', 20, 'bold'), activebackground=dth_clr, activeforeground='white', highlightthickness=0, bd=0, cursor='hand2', command=view_data_btn )
    View_btn.place(x=50, y=900)
    
    Add_rem_btn=tk.Button(iframe,text='Add Reminders', bg=dth_clr, fg=lfnt , font=('yu gothic ui', 20, 'bold'), activebackground=dth_clr, activeforeground='white', highlightthickness=0, bd=0, cursor='hand2',command=add_frame)
    Add_rem_btn.place(x=530, y=900)
    #------------------  Inner inner Frame  ---------------------------
    global iiframe
    iiframe=tk.Frame(iframe, bg=dth_clr)
    iiframe.place(x=220, y=400, width='1038', height='200')

    recent=tk.Label(iiframe, text='Recently Added',font=('yu gothic ui', 20, 'bold'), bg=dth_clr, fg=lfnt )
    recent.pack(side=tk.TOP)
    #--------------  Reminder Adding Section  --------------------- 
    down_frame=tk.Frame(iframe,width=1400,height=70,bg=dth_clr)
    down_frame.place(x=60,y=950)
    
# ----------------  Dashboard Heading  -------------------
    heading =tk.Label(iframe , text='Reminder',font=('yu gothic ui', 44, 'bold'),bg=dth_clr, fg=lfnt)
    heading.place(x=650, y=0)
    
#===========================  Calendar icon  ======================================
    calendar_icon=tk.PhotoImage(file='/home/rolen/Downloads/11/Images/calendar.png')
    calendar_icon_lbl=tk.Button(down_frame,image=calendar_icon, bg=dth_clr, activebackground=dth_clr, activeforeground=dth_clr, highlightthickness=0, bd=0, cursor='hand2', command=cal_toggle_open)
    calendar_icon_lbl.image=calendar_icon
    calendar_icon_lbl.place(x=1210,y=20)
#===========================  Alarm icon  ======================================
    alarm_icon=tk.PhotoImage(file='/home/rolen/Downloads/11/Images/alarm.png')
    alarm_icon_lbl=tk.Button(down_frame,image=alarm_icon, bg=dth_clr, activebackground=dth_clr, activeforeground=dth_clr, highlightthickness=0, bd=0, cursor='hand2', command=timepick )
    alarm_icon_lbl.image=alarm_icon
    alarm_icon_lbl.place(x=1270,y=17)

#===========================  Add Writing Area  ======================================

    tentry_var=tk.StringVar()
    global add_title
    add_title=tk.Entry(down_frame, font=('yu gothic ui', 20, 'bold'), fg=lth_clr, bg=dth_clr, bd=0 ,highlightthickness=0, textvariable=tentry_var, insertbackground=lth_clr, width=15)
    add_title.place(x=70,y=15)
    add_title.insert(0,'Reminder Title....')
    add_title.bind("<FocusIn>",on_rem_title_press)
    title_line=tk.Canvas(down_frame, width=260, height=2.0, bg=lfnt, highlightthickness=0)
    title_line.place(x=68, y=52)

    dentry_var=tk.StringVar()
    global add_description
    add_description=tk.Entry(down_frame, font=('yu gothic ui', 20, 'bold'), fg=lth_clr, bg=dth_clr, bd=0 ,highlightthickness=0, textvariable=dentry_var, insertbackground=lth_clr, width=20)
    add_description.place(x=400,y=15)
    add_description.insert(0,'Reminder Description....')
    add_description.bind("<FocusIn>",on_rem_description_press)
    title_line=tk.Canvas(down_frame, width=360, height=2.0, bg=lfnt, highlightthickness=0)
    title_line.place(x=400, y=52)

    global new_entry
    blank=('_'*8)+(' '*10)+('_'*8)+(' '*10)+('_'*8)+(' '*10)+('_'*8)
    new_entry=tk.Label(iiframe, bg=dialog_bg, text=blank, font=('yu gothic ui', 24, 'bold'), width=1098, height=2)
    new_entry.pack(side=tk.BOTTOM)
    
    add_button=tk.PhotoImage(file='/home/rolen/Downloads/11/Images/add.png')
    add_button_lbl=tk.Button(down_frame,image=add_button,bg=dth_clr,activebackground=dth_clr,activeforeground=dth_clr, highlightthickness=0, bd=0, cursor='hand2', command=recently_added_checklist)
    add_button_lbl.image=add_button
    add_button_lbl.place(x=16,y=16)

def note_frame():
    def on_note_title_press(str):
        title_entry.delete(0, tk.END)
    
    def noteview():
        note.delete('1.0', tk.END)
        conn=sqlite3.connect('reg_usrs.db')
        c=conn.cursor()

        c.execute("SELECT note FROM notes_table WHERE title=? AND belongs_to=?",[title_entry.get(), uid])
        txt = c.fetchall()
        try:
            note.insert( "1.0", txt[0][0])
        except:
            note.insert( "1.0", '')

    def notesave():
        txt=note.get( 1.0, tk.END)
        conn=sqlite3.connect('reg_usrs.db')
        c=conn.cursor()

        c.execute("SELECT title FROM notes_table WHERE title=? AND belongs_to=?",[title_entry.get(), uid])
        title= c.fetchall()
  
        if title == []:
            c.execute("INSERT INTO notes_table (title, note, belongs_to) VALUES (?, ?, ?)",[title_entry.get(),txt, uid])
            conn.commit()
        else:
            c.execute("UPDATE notes_table SET note=? WHERE title=? AND belongs_to=?",[txt, title_entry.get(),uid])
            conn.commit()
    
    def deletenote():
        conn=sqlite3.connect('reg_usrs.db')
        c=conn.cursor()
        c = conn.cursor()
        c.execute("DELETE FROM notes_table WHERE title=?",[tlevel_entry.get()])
        conn.commit()
        note.delete(1.0, tk.END)
        try:
            view_fr.destroy()
        except:
            pass
    
        view_titles()

    def delete_toplevel():
            view_titles()
            try:
                view_fr.destroy()
            except:
                pass
            view_titles()
            global ntop
            ntop=tk.Toplevel()
            ntop.geometry('400x150')
            ntop.title('Delete Note')
            ntop.config(bg=dth_clr)
            dialog_lbl=tk.Label(ntop,text="Enter the note title you want to delete", bg=dth_clr, fg=lfnt,font=('yu gothic ui', 12, 'bold'), pady=15)
            dialog_lbl.pack()

            global tlevel_entry
            tlevel_entry=tk.Entry(ntop,width=23,font="Arial, 12")
            tlevel_entry.pack()

            del_btn=tk.Button(ntop,text='DELETE',bg=dth_clr, fg=lfnt, font=('yu gothic ui', 12, 'bold') ,command=deletenote)
            del_btn.place(x=250,y=100)

            close_btn=tk.Button(ntop,text='OK',font=('yu gothic ui', 12, 'bold'), bg=dth_clr, fg=lfnt, command=lambda :ok(ntop))
            close_btn.place(x=340,y=100)

    def view_titles():
        conn=sqlite3.connect('reg_usrs.db')
        c=conn.cursor()

        global view_fr
        view_fr=tk.Frame(iframe, width=350, height=250, bg=dth_clr)
        view_fr.place(x=330, y=685)
        view_listbox = tk.Listbox(view_fr, font=('Arial', 12), selectmode=tk.NONE, bg=dth_clr, fg=lfnt, selectbackground=dth_clr, selectforeground=lfnt)
        view_listbox.pack(side=tk.TOP)
        
        view_listbox.delete(0, tk.END)
        c.execute("SELECT title FROM notes_table WHERE belongs_to=?",[uid])
        titles= c.fetchall()
        for i in range(len(titles)):
            view_listbox.insert(tk.END, titles[i][0])
        conn.commit()

        ok_button = tk.Button(view_fr, text="Close", bg=dialog_bg, fg=lfnt, highlightthickness=0, bd=0, command=lambda: ok(view_fr))
        ok_button.pack()
        


    dashfr_img=ImageTk.PhotoImage(Image.open('/home/rolen/Downloads/11/Images/dash_bg.png'))
    dash_bg=tk.Label(iframe, image=dashfr_img)
    dash_bg.image=dashfr_img
    dash_bg.pack(fill='both', expand='yes')

# ----------------  Dashboard Heading  -------------------
    heading =tk.Label(iframe , text='Sticky Notes',font=('yu gothic ui', 44, 'bold'),bg=dth_clr, fg=lfnt)
    heading.place(x=650, y=0)

# ===========================  Add Writing Area  ======================================   
    up_frame=tk.Frame(iframe,width=1202,height=68,bg=dialog_bg)
    up_frame.place(x=150,y=150)
    
    title_entry=tk.Entry(up_frame,width=20,font=('yu gothic ui', 22, 'bold'),bd=0, highlightthickness=0, bg=dialog_bg, fg=lfnt, insertbackground=lfnt)
    title_entry.place(x=420,y=16)
    title_entry.insert(0, 'Enter Note Title...')
    title_entry.bind("<FocusIn>",on_note_title_press)
    title_line=tk.Canvas(up_frame, width=400, height=2.0, bg=lfnt, highlightthickness=0)
    title_line.place(x=420, y=50)

    scrollbarY=tk.Scrollbar(iframe,orient=tk.VERTICAL, background=lth_clr, activebackground=lth_clr, troughcolor=dth_clr)
    scrollbarY.place(relx=0.8920,rely=0.189,width=12,height=685)

    note= tk.Text(iframe, width=100, height=28,font=('yu gothic ui', 14, 'bold'), bg=dialog_bg, fg=dfnt, insertbackground=dfnt, bd=0, highlightthickness=0, yscrollcommand=scrollbarY.set)
    note.place(x=150, y=220)
    note.insert(tk.END, "Add Notes...\n")

    down_frame=tk.Frame(iframe,width=1200,height=70,bg=dialog_bg)
    down_frame.place(x=155,y=930)
    
    save_note=tk. Button(down_frame, text='Save Note', font=('yu gothic ui', 20, 'bold'), bg=btn_bg, fg=lfnt, bd=0,cursor='hand2',activebackground=btn_bg,highlightthickness=0, command=notesave)
    save_note.place(x=10, y=16)
    
    Notes_list=tk. Button(down_frame, text='Notes List', font=('yu gothic ui', 20, 'bold'), bg=btn_bg, fg=lfnt, bd=0,cursor='hand2',activebackground=btn_bg,highlightthickness=0, command=view_titles)
    Notes_list.place(x=180, y=16)
    
    view_note=tk. Button(up_frame, text='View Note', font=('yu gothic ui', 20, 'bold'), bg=btn_bg, fg=lfnt, bd=0,cursor='hand2',activebackground=btn_bg,highlightthickness=0, command=noteview)
    view_note.place(x=900, y=16)

    delete_note=tk. Button(down_frame, text='Delete Note', font=('yu gothic ui', 20, 'bold'), bg=btn_bg, fg=lfnt, bd=0,cursor='hand2',activebackground=btn_bg,highlightthickness=0, command=delete_toplevel)
    delete_note.place(x=350, y=16)

def chk_frame():
    def on_chk_title_press(str):
        title_entry.delete(0, tk.END)

    def on_chk_desc_press(str):
        item_entry.delete(0, tk.END)

    def delete_chk():
        conn=sqlite3.connect('reg_usrs.db')
        c=conn.cursor()
        c = conn.cursor()
        c.execute("DELETE FROM checklist_table WHERE title=?",[clevel_entry.get()])
        conn.commit()

        view_fr.destroy()
        view_checklist()
        view_chk_titles()

    def delete_chk_toplevel():
            try:
                view_fr.destroy()
            except:
                pass
            view_chk_titles()
            global ntop
            ctop=tk.Toplevel()
            ctop.geometry('400x150')
            ctop.title('Delete Note')
            ctop.config(bg=dth_clr)
            dialog_lbl=tk.Label(ctop,text="Enter the checklist title you want to delete", bg=dth_clr, fg=lfnt,font=('yu gothic ui', 12, 'bold'), pady=15)
            dialog_lbl.pack()

            global clevel_entry
            clevel_entry=tk.Entry(ctop,width=23,font="Arial, 12")
            clevel_entry.pack()

            del_btn=tk.Button(ctop,text='DELETE',bg=dth_clr, fg=lfnt, font=('yu gothic ui', 12, 'bold') ,command=delete_chk)
            del_btn.place(x=250,y=100)

            close_btn=tk.Button(ctop,text='OK',font=('yu gothic ui', 12, 'bold'), bg=dth_clr, fg=lfnt, command=lambda :ok(ctop))
            close_btn.place(x=340,y=100)

    def view_chk_titles():
        conn=sqlite3.connect('reg_usrs.db')
        c=conn.cursor()

        global view_fr
        view_fr=tk.Frame(iframe, width=350, height=250, bg=dth_clr)
        view_fr.place(x=1250, y=520)
        view_listbox = tk.Listbox(view_fr, font=('Arial', 12), selectmode=tk.NONE, bg=dth_clr, fg=lfnt, selectbackground=dth_clr, selectforeground=lfnt)
        view_listbox.pack(side=tk.TOP)
        
        view_listbox.delete(0, tk.END)
        c.execute("SELECT title FROM checklist_table WHERE belongs_to=?",[uid])
        all_titles= c.fetchall()

        def Remove(duplicate):
            orgs = []
            for val in duplicate:
                if val not in orgs:
                    orgs.append(val)
            return orgs
        
        titles=Remove(all_titles)
        
        for i in range(len(titles)):
            view_listbox.insert(tk.END, titles[i][0])
        conn.commit()

        ok_button = tk.Button(view_fr, text="Close", bg=dialog_bg, fg=lfnt, highlightthickness=0, bd=0, command=lambda: ok(view_fr))
        ok_button.pack()



    def print_selection():
        selection = listbox.get(listbox.curselection())
        return selection
 
    def view_checklist():
        listbox.delete(0, tk.END)
        conn=sqlite3.connect('reg_usrs.db')
        c=conn.cursor()

        c.execute("SELECT items FROM checklist_table WHERE title=? AND belongs_to=?",[title_entry.get(),uid])
        items=c.fetchall()
        for i in range(len(items)):
            listbox.insert(tk.END, items[i][0])
    
    def add_checklist():
        listbox.delete(0, tk.END)
        conn=sqlite3.connect('reg_usrs.db')
        c=conn.cursor()
        c.execute("INSERT INTO checklist_table (title, items, belongs_to) VALUES (?, ?, ?)",[title_entry.get(), item_entry.get(), uid])
        c.execute("SELECT items FROM checklist_table WHERE belongs_to=? AND title=?",[uid, title_entry.get()])
        info= c.fetchall()
        for i in range(len(info)):
            listbox.insert(tk.END, info[i][0])
        conn.commit()

    def done_checklist():
        conn=sqlite3.connect('reg_usrs.db')
        c=conn.cursor()
        
        c = conn.cursor()
        c.execute("DELETE FROM checklist_table WHERE title=? AND belongs_to=? AND items=?",[title_entry.get(), uid, print_selection()])
        conn.commit()
        listbox.delete(tk.ANCHOR)

    dashfr_img=ImageTk.PhotoImage(Image.open('/home/rolen/Downloads/11/Images/dash_bg.png'))
    dash_bg=tk.Label(iframe, image=dashfr_img)
    dash_bg.image=dashfr_img
    dash_bg.pack(fill='both', expand='yes')

# ----------------  Dashboard Heading  -------------------
    heading =tk.Label(iframe , text='Check-List',font=('yu gothic ui', 44, 'bold'),bg=dth_clr, fg=lfnt)
    heading.place(x=650, y=0)

    cframe=tk.Frame(iframe, bd=3,width=1400,height=700,bg=dth_clr)
    cframe.place(x=280, y=200)

    up_frame=tk.Frame(iframe,width=880,height=70,bg=dth_clr)
    up_frame.place(x=280,y=150)

    down_frame=tk.Frame(iframe,width=1200,height=70,bg=dth_clr)
    down_frame.place(x=155,y=950)

    listbox=tk.Listbox(cframe,font=('yu gothic ui', 25, 'bold'),width=40,height=14,bg=dth_clr,fg=lfnt,cursor="hand2",selectbackground=dialog_bg)
    listbox.pack(side=tk.LEFT,fill=tk.BOTH,padx=25,pady=25)
    
    scrollbar=tk.Scrollbar(cframe)
    scrollbar.pack(side=tk.RIGHT,fill=tk.BOTH)
    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)
    listbox.bind("<<ListboxSelect>>", lambda event: print_selection())

    global title_entry
    title_entry=tk.Entry(up_frame,width=20,font=('yu gothic ui', 22, 'bold'),bd=0, highlightthickness=0,insertbackground=lfnt, bg=dth_clr, fg=lfnt)
    title_entry.place(x=150,y=28)
    title_entry.insert(0,'Enter the Checklist title ....')
    title_entry.bind("<FocusIn>",on_chk_title_press)

    title_line=tk.Canvas(cframe, width=390, height=2.0, bg=lfnt, highlightthickness=0)
    title_line.place(x=150, rely=0.025)

    item_entry=tk.Entry(down_frame,width=60,font=('yu gothic ui', 20, 'bold'),bd=0, highlightthickness=0, bg=dth_clr, fg=lfnt, insertbackground=lfnt)
    item_entry.place(x=65,y=16)
    item_entry.insert(0,'Enter the Checklist Description ....')
    item_entry.bind("<FocusIn>",on_chk_desc_press)
    item_line=tk.Canvas(down_frame, width=900, height=2.0, bg=lfnt, highlightthickness=0)
    item_line.place(x=65, y=50)

    Done_btn=tk.Button(iframe,text='Mark as done', bg=dth_clr, fg=lfnt , font=('yu gothic ui', 20, 'bold'), activebackground=lth_clr, activeforeground=dfnt, highlightthickness=0, bd=0, cursor='hand2', command=done_checklist)
    Done_btn.place(x=160, y=900)
    View_btn=tk.Button(up_frame,text='View Checklist Items', bg=dialog_bg, fg=lfnt , font=('yu gothic ui', 20, 'bold'), activebackground=lth_clr, activeforeground=dth_clr, highlightthickness=0, bd=0, cursor='hand2', command=view_checklist)
    View_btn.place(x=550, y=16)
    
    dele_btn=tk.Button(iframe,text='Delete Checklists', bg=dialog_bg, fg=lfnt , font=('yu gothic ui', 20, 'bold'), activebackground=lth_clr, activeforeground=dth_clr, highlightthickness=0, bd=0, cursor='hand2', command=delete_chk_toplevel)
    dele_btn.place(x=900, y=850)
    
    list_btn=tk.Button(iframe,text='View Checklists', bg=dialog_bg, fg=lfnt , font=('yu gothic ui', 20, 'bold'), activebackground=lth_clr, activeforeground=dth_clr, highlightthickness=0, bd=0, cursor='hand2', command=view_chk_titles)
    list_btn.place(x=1200, y=850)

    add_btn_img=tk.PhotoImage(file='/home/rolen/Downloads/11/Images/add.png')
    add_btn_lbl=tk.Button(down_frame,image=add_btn_img,bg=dth_clr,activebackground=dth_clr,activeforeground=dth_clr, highlightthickness=0, bd=0, cursor='hand2', command=add_checklist)
    add_btn_lbl.image=add_btn_img
    add_btn_lbl.place(x=16,y=16)

    warning=tk.Label(iframe,text="Items completed in the check list will be automatically deleted, Incomplete tasks remain",fg=lfnt, bg=dth_clr, font=('yu gothic ui', 20))
    warning.place(x=365,y=905)
def run_dashboard(user_data:dict): 
    chk_frontend(user_data)
    dash.mainloop()