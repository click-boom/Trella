from tkinter import *
from tkinter import Canvas
from PIL import Image, ImageTk
from datetime import *
import time

dash =tk.Tk()
dash.title('TRELLA')
dash.geometry('1280x1080')
dash.config(bg='#d6d6d6')
def dashboard():
        
        
        #adding icon
        icon=PhotoImage(file='D:\TRELLA\llogo.png')
        self.root.iconphoto(True, icon)
        
        #-------------------------------------------------------
        #----------------  HEADER   ----------------------------
        #-------------------------------------------------------
        
        self.header= Frame(self.root, bg='#748AC1')
        self.header.place(x=400, y=0, width=1650, height=120)
        
        
        #-------------------------------------------------------
        #----------------  SIDE BAR   --------------------------
        #-------------------------------------------------------    
        
        self.sidebar = Frame(self.root,
                             bg='#DFEAF6',
                             )    
        self.sidebar.place(x=0, y=0, width=400, height=1080)
        
        
        #-------------------------------------------------------
        #----------------  LOGOUT_button   ---------------------
        #-------------------------------------------------------        
        
        self.mode = Button(self.root, 
                                  text='Logout',
                                  bg='#DFEAF6', 
                                  font=('yu gothic ui', 13, ), 
                                  bd=0, 
                                  fg='BLACK',
                                  cursor='hand2',
                                  activebackground='#DFEAF6')
        self.mode.place(x=150, y=960)
        
        #-------------------------------------------------------
        #----------------  BODY  -------------------------------
        #-------------------------------------------------------  
        
        self.heading = Label(self.root, text='Dashboard',
                             font=('yu gothic ui', 40, 'bold'),
                             bg='#748AC1'
                            )
        self.heading.place(x=1050, y=20)
        
        
        
        #-------------------------------------------------------
        #----------------  logo  -------------------------------
        #-------------------------------------------------------  
        self.logoImage =Image.open('D:/TRELLA/llogo.png')
        photo= ImageTk.PhotoImage(self.logoImage)
        self.logo = Label(self.sidebar, image=photo,
                          bg='#DFEAF6')
        self.logo.image=photo
        self.logo.place(x=110, y=40)
        
        #-------------------------------------------------------
        #----------------  name of user ------------------------
        #-------------------------------------------------------  
        self.user = Label(self.sidebar, text='Hello Someone!',
                           font=('yu gothic ui', 30, 'bold', 'underline'),
                           bg='#DFEAF6'
                          )
        self.user.place(x=48, y=240)
        
        #-------------------------------------------------------
        #----------------  checklist_text ----------------------
        #-------------------------------------------------------  
        self.checklist_text= Button(self.sidebar, text='Checklist',
                            font=('yu gothic ui', 25, 'bold'),
                            bg='#DFEAF6',
                            cursor='hand2',
                            activebackground='#DFEAF6',
                            bd=0,
                            width=21
                            
                              )
        self.checklist_text.place(x=0, y=400)
        
        #-------------------------------------------------------
        #----------------  checklist_image ----------------------
        #------------------------------------------------------- 
        
        self.checklistImage= Image.open('D:/TRELLA/checklist.png')
        photo = ImageTk.PhotoImage(self.checklistImage)
        self.checklist= Label(self.checklist_text, image=photo, bg='#DFEAF6')
        self.checklist.image= photo
        self.checklist.place(x=0, y=20)
        
        
        #-------------------------------------------------------
        #----------------  reminder_text ----------------------
        #-------------------------------------------------------  
        self.reminder_text= Button(self.sidebar, text='Reminder',
                            font=('yu gothic ui', 25, 'bold'),
                            bg='#DFEAF6',
                            cursor='hand2',
                            activebackground='#DFEAF6',
                            bd=0,
                            width=21
                              )
        self.reminder_text.place(x=0, y=480)
        
        #-------------------------------------------------------
        #----------------  reminder_image ----------------------
        #------------------------------------------------------- 
        
        self.reminderImage= Image.open('D:/TRELLA/reminder.png')
        photo = ImageTk.PhotoImage(self.reminderImage)
        self.reminder= Label(self.reminder_text, image=photo, bg='#DFEAF6')
        self.reminder.image= photo
        self.reminder.place(x=0, y=20)


        #-------------------------------------------------------
        #----------------  Stickynotes_text ----------------------
        #-------------------------------------------------------  
        self.stickynotes_text= Button(self.sidebar, text='Sticky Notes',
                            font=('yu gothic ui', 25, 'bold'),
                            bg='#DFEAF6',
                            cursor='hand2',
                            activebackground='#DFEAF6',
                            bd=0,
                            width=21
                              )
        self.stickynotes_text.place(x=0, y=560)
        
        #-------------------------------------------------------
        #----------------  stickynotes_image ----------------------
        #------------------------------------------------------- 
        
        self.stickynotesImage= Image.open('D:/TRELLA/sticky_notes.png')
        photo = ImageTk.PhotoImage(self.stickynotesImage)
        self.stickynotes= Label(self.stickynotes_text, image=photo, bg='#DFEAF6')
        self.stickynotes.image= photo
        self.stickynotes.place(x=0, y=20)    
        
        #-------------------------------------------------------
        #----------------  calendar_text ----------------------
        #-------------------------------------------------------  
        self.calendar_text= Button(self.sidebar, text='Calendar',
                            font=('yu gothic ui', 25, 'bold'),
                            bg='#DFEAF6',
                            cursor='hand2',
                            activebackground='#DFEAF6',
                            bd=0,
                            width=21
                              )
        self.calendar_text.place(x=0, y=640)
        
        #-------------------------------------------------------
        #----------------  calendar_image ----------------------
        #------------------------------------------------------- 
        
        self.calendarImage= Image.open('D:/TRELLA/calendar.png')
        photo = ImageTk.PhotoImage(self.calendarImage)
        self.calendar= Label(self.calendar_text, image=photo, bg='#DFEAF6')
        self.calendar.image= photo
        self.calendar.place(x=0, y=20)     
        
        
        
        #-------------------------------------------------------
        #----------------  line ----------------------
        #------------------------------------------------------- 
        self.passwd_line=Canvas(self.sidebar, width=450, height=2.0,
                                bg='black', 
                                highlightthickness=0)
        self.passwd_line.place(x=0, y=397)
        
        self.passwd_line=Canvas(self.sidebar, width=450, height=2.0,
                                bg='black', 
                                highlightthickness=0)
        self.passwd_line.place(x=0, y=477)
        
        self.passwd_line=Canvas(self.sidebar, width=450, height=2.0,
                                bg='black', 
                                highlightthickness=0)
        self.passwd_line.place(x=0, y=557)
        
        self.passwd_line=Canvas(self.sidebar, width=450, height=2.0,
                                bg='black', 
                                highlightthickness=0)
        self.passwd_line.place(x=0, y=637)


        self.passwd_line=Canvas(self.sidebar, width=450, height=2.0,
                                bg='black', 
                                highlightthickness=0)
        self.passwd_line.place(x=0, y=717)
        
        #-------------------------------------------------------
        #----------------  mode_ones ---------------------------
        #------------------------------------------------------- 
        self.modeImage= Image.open('D:/TRELLA/white-half-circle.png')
        photo = ImageTk.PhotoImage(self.modeImage)
        self.mode= Button(self.sidebar, 
                          image=photo,
                          bg='#DFEAF6',
                          bd=0,
                          cursor='hand2',
                          activebackground='#DFEAF6')
        self.mode.image= photo
        self.mode.place(x=120, y=830)  

        self.modeImage= Image.open('D:/TRELLA/black-half-circle.png')
        photo = ImageTk.PhotoImage(self.modeImage)
        self.mode= Button(self.sidebar, 
                          image=photo,
                          bg='#DFEAF6',
                          bd=0,
                          cursor='hand2',
                          activebackground='#DFEAF6')
        self.mode.image= photo
        self.mode.place(x=178, y=830)  
        
        #-------------------------------------------------------
        #----------------  date and time -----------------------
        #------------------------------------------------------- 
        self.date_time = Label(self.root)
        self.date_time.place(x=150, y=315)
        self.show_time()
        
    def show_time(self):
        self.time = time.strftime('%H:%M:%S')
        self.date = time.strftime('%Y/%m/%d')
        set_text= f"{self.time} \n {self.date}"
        self.date_time.configure(text=set_text,
                                 font=('yu gothic ui', 15, 'bold'),
                                 bd=0,
                                 bg='#DFEAF6'
                                 )
        self.date_time.after(100, self.show_time)
        
        
        
def win():
    root= Tk()
    dashboard(root)
    root.mainloop()



if __name__ == '__main__':
    win()