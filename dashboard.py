import tkinter as tk
from PIL import Image, ImageTk
import time

dash =tk.Tk()
dash.title('TRELLA')
dash.geometry('1280x1080')
dash.config(bg='#d6d6d6')
def dashboard():
        
        #----------------  Titlebar Icon   -----------------------
        
        icon=tk.PhotoImage(file='/home/wae/Documents/giri raj sir/Trella/Images/llogo.png')
        dash .iconphoto(True, icon)
        
        #-------------------  Theme  -----------------------------
            
        lth_clr='#A0B6E9'
        dth_clr='#4C6195'
        fnt='#6c6c6c'
        btn_bg='#a4a4a4'


        #-------------------  Heading Bar  ------------------------
        
        header= tk.Frame(dash , bg=lth_clr)
        header.place(x=400, y=0, width=1650, height=120)
        
        #----------------  SIDE BAR   --------------------------
        
        sidebar =tk.Frame(dash ,bg=dth_clr)    
        sidebar.place(x=0, y=0, width=400, height=1080)
        
        #----------------  Dashboard Heading  -------------------
        heading =tk.Label(dash , text='Dashboard',font=('yu gothic ui', 40, 'bold'),bg=lth_clr)
        heading.place(x=1050, y=20)
        
        #----------------  LOGOUT_button   ---------------------

        # mode =tk.Button(dash ,text='Logout',bg='#DFEAF6', font=('yu gothic ui', 13, ), bd=0, fg='BLACK',cursor='hand2',activebackground='#DFEAF6')
        # mode.place(x=150, y=960)
          
        
        #----------------  Logo  -------------------------------  
      
        logo_Img= ImageTk.PhotoImage(Image.open('/home/wae/Documents/giri raj sir/Trella/Images/llogo.png'))
        logo =tk.Label(sidebar,
                image=logo_Img ,
                
                bg=dth_clr)
        logo.image=logo_Img
        logo.place(x=125, y=60)
      
        #----------------  Username and its Label -------------------------------  
        
      
        btn_img=tk.PhotoImage(Image.open('/home/wae/Documents/giri raj sir/Trella/Images/dash_btn.png'))    
        dash_user_btn=tk.Label(sidebar,image=btn_img)
        dash_user_btn.image=btn_img
        dash_user_btn.place(x=225, y=510)

        login_btn=tk.Button(btn_img, text='Sign in', font=('yu gothic ui', 18, 'bold'),width=10, bd=0, highlightthickness=0,  bg=btn_bg, cursor='hand2', activebackground=btn_bg, fg='white' )
        login_btn.place(x=30, y=8)


        #----------------  Username and its Label -------------------------------  


      
      
      





      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
        #----------------  checklist_text ----------------------

        # chklst_img=tk.PhotoImage(file=('/home/wae/Documents/giri raj sir/Trella/Images/check-list.png'))    
        # login_btn_img=tk.Label(login_frame,image=btn_img)
        # login_btn_img.image=btn_img
        # login_btn_img.place(x=225, y=510)

        # login_btn=tk.Button(login_btn_img, text='Sign in', font=('yu gothic ui', 18, 'bold'),width=10, bd=0, highlightthickness=0,  bg=btn_bg, cursor='hand2', activebackground=btn_bg, fg='white' )
        # login_btn.place(x=30, y=8)

        
        # #----------------  checklist_image ----------------------
         
        # dash.checklistImage= Image.open('/home/wae/Documents/giri raj sir/Trella/Images/check-list.png')
        # photo = ImageTk.PhotoImage(dash.checklistImage)
        # dash.checklist= tk.Label(dash.checklist_text, image=photo, bg='#DFEAF6')
        # dash.checklist.image= photo
        # dash.checklist.place(x=0, y=20)
        
        # #----------------  Reminder_text ----------------------
          
        # dash.reminder_text=tk.Button(sidebar, text='Reminder',font=('yu gothic ui', 25, 'bold'),bg='#DFEAF6',cursor='hand2',activebackground='#DFEAF6',bd=0,width=21)
        # dash.reminder_text.place(x=0, y=480)
        
        # #----------------  Reminder_image ----------------------
         
        # dash.reminderImage= Image.open('/home/wae/Documents/giri raj sir/Trella/Images/reminder.png')
        # photo = ImageTk.PhotoImage(dash.reminderImage)
        # dash.reminder=tk.Label(dash.reminder_text, image=photo, bg='#DFEAF6')
        # dash.reminder.image= photo
        # dash.reminder.place(x=0, y=20)

        # #----------------  Stickynotes_text ----------------------
  
        # dash.stickynotes_text=tk.Button(sidebar, text='Sticky Notes',font=('yu gothic ui', 25, 'bold'),bg='#DFEAF6',cursor='hand2',activebackground='#DFEAF6',bd=0, width=21)
        # dash.stickynotes_text.place(x=0, y=560)
        
        # #----------------  Stickynotes_image ----------------------
        
        # dash.stickynotesImage= Image.open('/home/wae/Documents/giri raj sir/Trella/Images/sticky-note.png')
        # photo = ImageTk.PhotoImage(dash.stickynotesImage)
        # dash.stickynotes=tk.Label(dash.stickynotes_text, image=photo, bg='#DFEAF6')
        # dash.stickynotes.image= photo
        # dash.stickynotes.place(x=0, y=20)    
        
        # #----------------  Calendar_text ----------------------
  
        # dash.calendar_text= tk.Button(sidebar, text='Calendar',font=('yu gothic ui', 25, 'bold'),bg='#DFEAF6',cursor='hand2',activebackground='#DFEAF6',bd=0,width=21)
        # dash.calendar_text.place(x=0, y=640)
        
        # #----------------  Calendar_image ----------------------
         
        # dash.calendarImage= Image.open('/home/wae/Documents/giri raj sir/Trella/Images/calendar.png')
        # photo = ImageTk.PhotoImage(dash.calendarImage)
        # dash.calendar=tk.Label(dash.calendar_text, image=photo, bg='#DFEAF6')
        # dash.calendar.image= photo
        # dash.calendar.place(x=0, y=20)     
        
        # #----------------  Line ----------------------
         
        # dash.passwd_line=tk.Canvas(sidebar, width=450, height=2.0,bg='black', highlightthickness=0)
        # dash.passwd_line.place(x=0, y=397)
        
        # dash.passwd_line=tk.Canvas(sidebar, width=450, height=2.0,bg='black', highlightthickness=0)
        # dash.passwd_line.place(x=0, y=477)
        
        # dash.passwd_line=tk.Canvas(sidebar, width=450, height=2.0,bg='black', highlightthickness=0)
        # dash.passwd_line.place(x=0, y=557)
        
        # dash.passwd_line=tk.Canvas(sidebar, width=450, height=2.0,bg='black', highlightthickness=0)
        # dash.passwd_line.place(x=0, y=637)


        # dash.passwd_line=tk.Canvas(sidebar, width=450, height=2.0,bg='black', highlightthickness=0)
        # dash.passwd_line.place(x=0, y=717)
        
        # #----------------  mode_ones  ---------------------------
         
        # dash.modeImage= Image.open('/home/wae/Documents/giri raj sir/Trella/Images/half-wcircle.png')
        # photo = ImageTk.PhotoImage(dash.modeImage)
        # dash.mode=tk.Button(sidebar, image=photo,bg='#DFEAF6',bd=0,cursor='hand2',activebackground='#DFEAF6')
        # dash.mode.image= photo
        # dash.mode.place(x=120, y=830)  

        # dash.modeImage= Image.open('/home/wae/Documents/giri raj sir/Trella/Images/half-bcircle.png')
        # photo = ImageTk.PhotoImage(dash.modeImage)
        # dash.mode= tk.Button(sidebar, image=photo,bg='#DFEAF6',bd=0,cursor='hand2',activebackground='#DFEAF6')
        # dash.mode.image= photo
        # dash.mode.place(x=178, y=830)  
        
        # #----------------  date and time  -----------------------
         
        # # dash.date_time = tk.Label(dash )
        # # dash.date_time.place(x=150, y=315)
        # # def show_time():
        # #   dash.time = time.strftime('%H:%M:%S')
        # #   dash.date = time.strftime('%Y/%m/%d')
        # # set_text= f"{dash.time} \n {dash.date}"
        # # dash.date_time.configure(text=set_text,
        # #                          font=('yu gothic ui', 15, 'bold'),
        # #                          bd=0,
        # #                          bg='#DFEAF6'
        # #                          )
        # # dash.date_time.after(100, dash.show_time)
        # # show_time()


dashboard()
dash.mainloop()