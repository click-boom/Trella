
import tkinter as tk
from PIL import Image, ImageTk
import time

dash =tk.Tk()
dash.title('TRELLA')
dash.geometry('1280x1080')
dash.config(bg='#d6d6d6')
def dashboard():
        
        icon=tk.PhotoImage(file='/home/wae/Documents/giri raj sir/Trella/Images/llogo.png')
        dash.root.iconphoto(True, icon)
        
        #----------------  HEADER   ----------------------------
        
        dash.header= tk.Frame(dash.root, bg='#748AC1')
        dash.header.place(x=400, y=0, width=1650, height=120)
        
        #----------------  SIDE BAR   --------------------------
        
        dash.sidebar =tk.Frame(dash.root,bg='#DFEAF6')    
        dash.sidebar.place(x=0, y=0, width=400, height=1080)
        
        #----------------  LOGOUT_button   ---------------------

        dash.mode =tk.Button(dash.root,text='Logout',bg='#DFEAF6', font=('yu gothic ui', 13, ), bd=0, fg='BLACK',cursor='hand2',activebackground='#DFEAF6')
        dash.mode.place(x=150, y=960)
          
        #----------------  BODY  -------------------------------
        
        dash.heading =tk.Label(dash.root, text='Dashboard',font=('yu gothic ui', 40, 'bold'),bg='#748AC1')
        dash.heading.place(x=1050, y=20)
        
        #----------------  logo  -------------------------------  
        dash.logoImage =Image.open('/home/wae/Documents/giri raj sir/Trella/Images/llogo.png')
        photo= ImageTk.PhotoImage(dash.logoImage)
        dash.logo =tk.Label(dash.sidebar, image=photo,bg='#DFEAF6')
        dash.logo.image=photo
        dash.logo.place(x=110, y=40)
        
        #----------------  Name Of User ------------------------  
        
        dash.user = tk.Label(dash.sidebar, text='Hello Someone!',font=('yu gothic ui', 30, 'bold', 'underline'),bg='#DFEAF6')
        dash.user.place(x=48, y=240)
        
        #----------------  checklist_text ----------------------
          
        dash.checklist_text=tk.Button(dash.sidebar, text='Checklist',font=('yu gothic ui', 25, 'bold'),bg='#DFEAF6',cursor='hand2',activebackground='#DFEAF6',bd=0,width=21)
        dash.checklist_text.place(x=0, y=400)
        
        #----------------  checklist_image ----------------------
         
        dash.checklistImage= Image.open('D:/TRELLA/checklist.png')
        photo = ImageTk.PhotoImage(dash.checklistImage)
        dash.checklist= tk.Label(dash.checklist_text, image=photo, bg='#DFEAF6')
        dash.checklist.image= photo
        dash.checklist.place(x=0, y=20)
        
        #----------------  Reminder_text ----------------------
          
        dash.reminder_text=tk.Button(dash.sidebar, text='Reminder',font=('yu gothic ui', 25, 'bold'),bg='#DFEAF6',cursor='hand2',activebackground='#DFEAF6',bd=0,width=21)
        dash.reminder_text.place(x=0, y=480)
        
        #----------------  Reminder_image ----------------------
         
        dash.reminderImage= Image.open('D:/TRELLA/reminder.png')
        photo = ImageTk.PhotoImage(dash.reminderImage)
        dash.reminder=tk.Label(dash.reminder_text, image=photo, bg='#DFEAF6')
        dash.reminder.image= photo
        dash.reminder.place(x=0, y=20)

        #----------------  Stickynotes_text ----------------------
  
        dash.stickynotes_text=tk.Button(dash.sidebar, text='Sticky Notes',font=('yu gothic ui', 25, 'bold'),bg='#DFEAF6',cursor='hand2',activebackground='#DFEAF6',bd=0, width=21)
        dash.stickynotes_text.place(x=0, y=560)
        
        #----------------  Stickynotes_image ----------------------
        
        dash.stickynotesImage= Image.open('D:/TRELLA/sticky_notes.png')
        photo = ImageTk.PhotoImage(dash.stickynotesImage)
        dash.stickynotes=tk.Label(dash.stickynotes_text, image=photo, bg='#DFEAF6')
        dash.stickynotes.image= photo
        dash.stickynotes.place(x=0, y=20)    
        
        #----------------  Calendar_text ----------------------
  
        dash.calendar_text= tk.Button(dash.sidebar, text='Calendar',font=('yu gothic ui', 25, 'bold'),bg='#DFEAF6',cursor='hand2',activebackground='#DFEAF6',bd=0,width=21)
        dash.calendar_text.place(x=0, y=640)
        
        #----------------  Calendar_image ----------------------
         
        dash.calendarImage= Image.open('D:/TRELLA/calendar.png')
        photo = ImageTk.PhotoImage(dash.calendarImage)
        dash.calendar=tk.Label(dash.calendar_text, image=photo, bg='#DFEAF6')
        dash.calendar.image= photo
        dash.calendar.place(x=0, y=20)     
        
        #----------------  Line ----------------------
         
        dash.passwd_line=tk.Canvas(dash.sidebar, width=450, height=2.0,bg='black', highlightthickness=0)
        dash.passwd_line.place(x=0, y=397)
        
        dash.passwd_line=tk.Canvas(dash.sidebar, width=450, height=2.0,bg='black', highlightthickness=0)
        dash.passwd_line.place(x=0, y=477)
        
        dash.passwd_line=tk.Canvas(dash.sidebar, width=450, height=2.0,bg='black', highlightthickness=0)
        dash.passwd_line.place(x=0, y=557)
        
        dash.passwd_line=tk.Canvas(dash.sidebar, width=450, height=2.0,bg='black', highlightthickness=0)
        dash.passwd_line.place(x=0, y=637)


        dash.passwd_line=tk.Canvas(dash.sidebar, width=450, height=2.0,bg='black', highlightthickness=0)
        dash.passwd_line.place(x=0, y=717)
        
        #----------------  mode_ones ---------------------------
         
        dash.modeImage= Image.open('D:/TRELLA/white-half-circle.png')
        photo = ImageTk.PhotoImage(dash.modeImage)
        dash.mode=tk.Button(dash.sidebar, image=photo,bg='#DFEAF6',bd=0,cursor='hand2',activebackground='#DFEAF6')
        dash.mode.image= photo
        dash.mode.place(x=120, y=830)  

        dash.modeImage= Image.open('D:/TRELLA/black-half-circle.png')
        photo = ImageTk.PhotoImage(dash.modeImage)
        dash.mode= tk.Button(dash.sidebar, image=photo,bg='#DFEAF6',bd=0,cursor='hand2',activebackground='#DFEAF6')
        dash.mode.image= photo
        dash.mode.place(x=178, y=830)  
        
        #----------------  date and time -----------------------
         
        dash.date_time = tk.Label(dash.root)
        dash.date_time.place(x=150, y=315)
        dash.show_time()
        def show_time(dash):
          dash.time = time.strftime('%H:%M:%S')
          dash.date = time.strftime('%Y/%m/%d')
        set_text= f"{dash.time} \n {dash.date}"
        dash.date_time.configure(text=set_text,
                                 font=('yu gothic ui', 15, 'bold'),
                                 bd=0,
                                 bg='#DFEAF6'
                                 )
        dash.date_time.after(100, dash.show_time)

dashboard()
dash.mainloop()


