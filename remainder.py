import tkinter as tk
from PIL import ImageTk, Image
from tkinter import Canvas
from tkinter import ttk
from datetime import *
reminder=tk.Tk()

#........................defining
# reminder....................
def dashboard():

    reminder.title('Trella')
    reminder.geometry('1920x1080')
    reminder.state("zoomed")
    reminder.config(background='#d6d6d6')

#.....................header....................
    
    header=tk.Frame(reminder, bg='#748AC1')
    header.place(x=400, y=0, width=1650, height=120)

#.....................top image....................
    trella_icon=tk.PhotoImage(file='D:/trela/Images/dlogo.png')

    reminder.iconphoto(True,trella_icon)

#.....................sidebar....................

    sidebar = tk.Frame(reminder,bg='#DFEAF6')
    sidebar.place(x=0, y=0, width=400, height=1080) 

#.....................logo_in_sidebar....................
    user_logo =Image.open('D:/trela/Images/dlogo.png')
    photo= ImageTk.PhotoImage(user_logo)
    logo =tk. Label(sidebar, image=photo,
                          bg='#DFEAF6')
    logo.image=photo
    logo.place(x=110, y=40)

#.....................logo_in_sidebar....................
    user =tk. Label(sidebar, text='Hello Someone!',
                           font=('Alegreya sans', 29, 'italic', 'underline'),
                           bg='#DFEAF6'
                          )
    user.place(x=48, y=240)

#.....................checklist_sidebar....................

    checklist_text= tk.Button(sidebar, text='Checklist',
                            font=('Segoe Script', 20, 'bold'),
                            bg='#DFEAF6',
                            cursor='hand2',
                            activebackground='#DFEAF6',
                            bd=0,
                            width=19
                            
                              )
    checklist_text.place(x=0, y=400)


    checklistImage= Image.open('D:/trela/Images/checklist.png')
    photo =ImageTk.PhotoImage(checklistImage)
    checklist= tk.Label(checklist_text, image=photo, bg='#DFEAF6')
    checklist.image= photo
    checklist.place(x=5, y=20)

    checklist_line=tk.Canvas(sidebar, width=450, height=2.0,
                                bg='black', 
                                highlightthickness=0)
    checklist_line.place(x=0, y=397)

    checklist_line=tk.Canvas(sidebar, width=450, height=2.0,
                                bg='black', 
                                highlightthickness=0)
    checklist_line.place(x=0, y=477)

#.....................remainder_sidebar....................
    reminder_text= tk.Button(sidebar, text='Reminder',
                            font=('Segoe Script', 20, 'bold'),
                            bg='#DFEAF6',
                            cursor='hand2',
                            activebackground='#DFEAF6',
                            bd=0,
                            width=20,fg="Blue"
                              )
    reminder_text.place(x=0, y=480)

    reminderImage= Image.open('D:/trela/Images/reminder.png')
    photo = ImageTk.PhotoImage(reminderImage)
    reminderimg=tk. Label(reminder_text, image=photo, bg='#DFEAF6')
    reminderimg.image= photo
    reminderimg.place(x=0, y=20)

    remainder_line=tk.Canvas(sidebar, width=450, height=2.0,
                                bg='black', 
                                highlightthickness=0)
    remainder_line.place(x=0, y=557)

    remainder_line=tk.Canvas(sidebar, width=450, height=2.0,
                                bg='black', 
                                highlightthickness=0)
    remainder_line.place(x=0, y=637)
        
#.....................stickynotes_sidebar......................

    stickynotes_text=tk. Button(sidebar, text='Sticky Notes',
                            font=('Segoe Script', 20, 'bold'),
                            bg='#DFEAF6',
                            cursor='hand2',
                            activebackground='#DFEAF6',
                            bd=0,
                            width=20
                              )
    stickynotes_text.place(x=0, y=560)

    stickynotesImage= Image.open('D:/trela/Images/sticky_notes.png')
    photo = ImageTk.PhotoImage(stickynotesImage)
    stickynotes=tk. Label(stickynotes_text, image=photo, bg='#DFEAF6')
    stickynotes.image= photo
    stickynotes.place(x=0, y=20) 

#.....................calender_sidebar......................
    calendar_text=tk. Button(sidebar, text='Calendar',
                            font=('Segoe Script', 20, 'bold'),
                            bg='#DFEAF6',
                            cursor='hand2',
                            activebackground='#DFEAF6',
                            bd=0,
                            width=20
                              )
    calendar_text.place(x=0, y=640)


    calendarImage= Image.open('D:/trela/Images/mail.png')
    photo = ImageTk.PhotoImage(calendarImage)
    calendar=tk. Label(calendar_text, image=photo, bg='#DFEAF6')
    calendar.image= photo
    calendar.place(x=0, y=20)

    passwd_line=Canvas(sidebar, width=450, height=2.0,
                                bg='black', 
                                highlightthickness=0)
    passwd_line.place(x=0, y=717)

#.....................darkmode _sidebar......................

    modeImage= Image.open('D:/trela/Images/white-half-circle.png')
    photo = ImageTk.PhotoImage(modeImage)
    mode=tk. Button(sidebar, 
                          image=photo,
                          bg='#DFEAF6',
                          bd=0,
                          cursor='hand2',
                          activebackground='#DFEAF6')
    mode.image= photo
    mode.place(x=120, y=840)  

    modeImage= Image.open('D:/trela/Images/black-half-circle.png')
    photo = ImageTk.PhotoImage(modeImage)
    mode=tk. Button(sidebar, 
                          image=photo,
                          bg='#DFEAF6',
                          bd=0,
                          cursor='hand2',
                          activebackground='#DFEAF6')
    mode.image= photo
    mode.place(x=178, y=840) 

#.....................timing _sidebar......................

    # date_time =tk. Label(reminder)
    # date_time.place(x=150, y=315)
    # show_time()
        
    # def show_time(self):
    #     self.time = tk.strftime('%H:%M:%S')
    #     self.date = tk.strftime('%Y/%m/%d')
    #     set_text= f"{self.time} \n {self.date}"
    #     self.date_time.configure(text=set_text,
    #                              font=('yu gothic ui', 15, 'bold'),
    #                              bd=0,
    #                              bg='#DFEAF6'
    #                              )
    #     self.date_time.after(100, self.show_time)

    mode =tk. Button(reminder, 
                    text='Logout',
                        bg='#DFEAF6', 
                        font=('Segoe Script', 13, ), 
                        bd=0, 
                        fg='BLACK',
                        cursor='hand2',
                    activebackground='#DFEAF6')
    mode.place(x=150, y=960)

#...................topic.........................
    heading =tk. Label(reminder, text='Reminder',
                             font=(' yu gothic ui', 40, 'bold'),
                             bg='#748AC1'
                            )
    heading.place(x=1050, y=20)

#....................image_image_user.....................
    remind_me_img=Image.open('D:/trela/Images/circle.png')
    remind_photo=ImageTk.PhotoImage(remind_me_img)
    remind_eidit=tk.Label(reminder,image=remind_photo,bg="#d6d6d6")
    remind_eidit.image=remind_photo
    remind_eidit.place(x=470,y=250)

    remind_me_text=tk.Button(reminder,text="Remind me",
                                font=(' yu gothic ui', 25,'bold'),
                                cursor="hand2",bd=0,bg="#d6d6d6",activebackground="#d6d6d6",width=13)
    remind_me_text.place(x=540,y=228)

    # remind_me_frame=tk.Frame(reminder,width="1400",height="750",bg="#6299D9")
    # remind_me_frame.place(x=500,y=290)



#....................add the text img button_user.....................

    add_me_img=Image.open('D:/trela/Images/add.png')
    add_photo=ImageTk.PhotoImage(add_me_img)
    add_eidit=tk.Label(reminder,image=add_photo,bg="#d6d6d6")
    add_eidit.image=add_photo
    add_eidit.place(x=470,y=330)

    add_me_text=tk.Button(reminder,text="Add text",
                                font=(' yu gothic ui', 23,'bold'),
                                cursor="hand2",bd=0,bg="#d6d6d6",activebackground="#d6d6d6",width=13)
    add_me_text.place(x=524,y=295)


#....................add to my day img button_user.....................
    day_me_img=Image.open('D:/trela/Images/sunny-day.png')
    day_photo=ImageTk.PhotoImage(day_me_img)
    day_eidit=tk.Label(reminder,image=day_photo,bg="#d6d6d6")
    day_eidit.image=day_photo
    day_eidit.place(x=470,y=410)

    day_me_text=tk.Button(reminder,text="Add to my Day",
                                font=(' yu gothic ui', 23,'bold'),
                                cursor="hand2",bd=0,bg="#d6d6d6",activebackground="#d6d6d6",width=13)
    day_me_text.place(x=573,y=378)

#....................add to my day img button_user.....................
    due_me_img=Image.open('D:/trela/Images/date-of-birth.png')
    due_photo=ImageTk.PhotoImage(due_me_img)
    due_eidit=tk.Label(reminder,image=due_photo,bg="#d6d6d6")
    due_eidit.image=due_photo
    due_eidit.place(x=470,y=490)

    due_me_text=tk.Button(reminder,text="My Day",
                                font=(' yu gothic ui', 23,'bold'),
                                cursor="hand2",bd=0,bg="#d6d6d6",activebackground="#d6d6d6",width=13)
    due_me_text.place(x=510,y=460)

#....................repeat img button_user.....................
    repeat_me_img=Image.open('D:/trela/Images/repeat.png')
    repeat_photo=ImageTk.PhotoImage(repeat_me_img)
    repeat_eidit=tk.Label(reminder,image=repeat_photo,bg="#d6d6d6")
    repeat_eidit.image=repeat_photo
    repeat_eidit.place(x=470,y=570)

    repeat_me_text=tk.Button(reminder,text="Repeat",
                                font=(' yu gothic ui', 23,'bold'),
                                cursor="hand2",bd=0,bg="#d6d6d6",activebackground="#d6d6d6",width=13)
    repeat_me_text.place(x=500,y=542)

#....................Attached file_img button_user.....................
    Attached_me_img=Image.open('D:/trela/Images/file.png')
    Attached_photo=ImageTk.PhotoImage(Attached_me_img)
    Attached_eidit=tk.Label(reminder,image=Attached_photo,bg="#d6d6d6")
    Attached_eidit.image=Attached_photo
    Attached_eidit.place(x=470,y=650)

    Attached_me_text=tk.Button(reminder,text="Attach a file",
                                font=('yu gothic ui', 23,'bold'),
                                cursor="hand2",bd=0,bg="#d6d6d6",activebackground="#d6d6d6",width=13)
    Attached_me_text.place(x=537,y=624)


#....................add notes file_img button_user.....................
    notes_me_img=Image.open('D:/trela/Images/notes.png')
    notes_photo=ImageTk.PhotoImage(notes_me_img)
    notes_eidit=tk.Label(reminder,image=notes_photo,bg="#d6d6d6")
    notes_eidit.image=notes_photo
    notes_eidit.place(x=470,y=730)

    notes_me_text=tk.Button(reminder,text="Add Notes",
                                font=('yu gothic ui', 23,'bold'),
                                cursor="hand2",bd=0,bg="#d6d6d6",activebackground="#d6d6d6",width=13)
    notes_me_text.place(x=523,y=706)
dashboard()
reminder.mainloop()
