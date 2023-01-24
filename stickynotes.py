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
    trella_icon=tk.PhotoImage(file='D:/TRELLA/Images/dlogo.png')

    reminder.iconphoto(True,trella_icon)

#.....................sidebar....................

    sidebar = tk.Frame(reminder,bg='#DFEAF6')
    sidebar.place(x=0, y=0, width=400, height=1080) 

#.....................logo_in_sidebar....................
    user_logo =Image.open('D:/TRELLA/Images/dlogo.png')
    photo= ImageTk.PhotoImage(user_logo)
    logo =tk. Label(sidebar, image=photo,
                          bg='#DFEAF6')
    logo.image=photo
    logo.place(x=110, y=40)

#.....................logo_in_sidebar....................
    user =tk. Label(sidebar, text='Hello Someone!',
                           font=('yu gothic ui', 29,  'underline'),
                           bg='#DFEAF6'
                          )
    user.place(x=48, y=240)

#.....................checklist_sidebar....................

    checklist_text= tk.Button(sidebar, text='Checklist',
                            font=('yu gothic ui', 25, 'bold'),
                            bg='#DFEAF6',
                            cursor='hand2',
                            activebackground='#DFEAF6',
                            bd=0,
                            width=19
                            
                              )
    checklist_text.place(x=0, y=400)


    checklistImage= Image.open('D:/TRELLA/Images/check-list.png')
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
                            font=('yu gothic ui', 25, 'bold'),
                            bg='#DFEAF6',
                            cursor='hand2',
                            activebackground='#DFEAF6',
                            bd=0,
                            width=20
                              )
    reminder_text.place(x=0, y=480)

    reminderImage= Image.open('D:/TRELLA/Images/reminder.png')
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
       
#.....................Images_sidebar......................


    Images_text=tk. Button(sidebar, text='Sticky Notes',
                            font=('yu gothic ui', 25, 'bold'),
                            bg='#DFEAF6',
                            cursor='hand2',
                            activebackground='#DFEAF6',
                            bd=0,
                            width=20, 
                            fg='blue'
                              )
    Images_text.place(x=0, y=560)

    ImagesImage= Image.open('D:/TRELLA/Images/sticky-note.png')
    photo = ImageTk.PhotoImage(ImagesImage)
    Images=tk. Label(Images_text, image=photo, bg='#DFEAF6')
    Images.image= photo
    Images.place(x=0, y=20) 

#.....................calender_sidebar......................
    calendar_text=tk. Button(sidebar, text='Calendar',
                            font=('yu gothic ui', 25, 'bold'),
                            bg='#DFEAF6',
                            cursor='hand2',
                            activebackground='#DFEAF6',
                            bd=0,
                            width=20
                              )
    calendar_text.place(x=0, y=640)


    calendarImage= Image.open('D:/TRELLA/Images/calendar.png')
    photo = ImageTk.PhotoImage(calendarImage)
    calendar=tk. Label(calendar_text, image=photo, bg='#DFEAF6')
    calendar.image= photo
    calendar.place(x=0, y=20)

    passwd_line=Canvas(sidebar, width=450, height=2.0,
                                bg='black', 
                                highlightthickness=0)
    passwd_line.place(x=0, y=717)

# #.....................darkmode _sidebar......................

#     modeImage= Image.open('D:/TRELLA/Images/white-half-circle.png')
#     photo = ImageTk.PhotoImage(modeImage)
#     mode=tk. Button(sidebar, 
#                           image=photo,
#                           bg='#DFEAF6',
#                           bd=0,
#                           cursor='hand2',
#                           activebackground='#DFEAF6')
    # mode.image= photo
    # mode.place(x=120, y=840)  

    # modeImage= Image.open('D:/TRELLA/Images/black-half-circle.png')
    # photo = ImageTk.PhotoImage(modeImage)
    # mode=tk. Button(sidebar, 
    #                       image=photo,
    #                       bg='#DFEAF6',
    #                       bd=0,
    #                       cursor='hand2',
    #                       activebackground='#DFEAF6')
    # mode.image= photo
    # mode.place(x=178, y=840) 

#.....................timing _sidebar......................

    # date_time =tk.Label(reminder)
    # date_time.place(x=150, y=315)
    # show_time()
        
    # def show_time(root):
    #     root.time = tk.strftime('%H:%M:%S')
    #     root.date = tk.strftime('%Y/%m/%d')
    #     set_text= f"{root.time} \n {root.date}"
    #     root.date_time.configure(text=set_text,
    #                              font=('yu gothic ui', 15, 'bold'),
    #                              bd=0,
    #                              bg='#DFEAF6'
    #                              )
    #     root.date_time.after(100, root.show_time)

    mode =tk. Button(reminder, 
                    text='Logout',
                        bg='#DFEAF6', 
                        font=('yu gothic ui', 13, ), 
                        bd=0, 
                        fg='BLACK',
                        cursor='hand2',
                    activebackground='#DFEAF6')
    mode.place(x=150, y=960)

#...................topic.........................
    heading =tk. Label(reminder, text='Sticky Notes',
                             font=('yu gothic ui', 40, 'bold'),
                             bg='#748AC1'
                            )
    heading.place(x=1050, y=20)

    top_line=tk.Canvas(reminder, width=1920, height=2.0,
                                bg='black', 
                                highlightthickness=0)
    top_line.place(x=400, y=945)
    
    bottom_line=tk.Canvas(reminder, width=1920, height=2.0,
                                bg='black', 
                                highlightthickness=0)
    bottom_line.place(x=400, y=1015)

# ...................create_button.........................
    create= tk.Button(reminder, text='Create',
                                font=('yu gothic ui', 15, 'bold'),
                                bg='#DFEAF6',
                                bd=0,
                                cursor='hand2',
                                activebackground='#DFEAF6',
                                width='10'
                      )
    create.place(x=450, y=960)
    
# ...................A-icon.........................
    Aicon= Image.open('D://TRELLA/Images/A.png')
    photo = ImageTk.PhotoImage(Aicon)
    a=tk. Button(reminder, 
                          image=photo,
                          bg='#d6d6d6',
                          bd=0,
                          cursor='hand2',
                          activebackground='#d6d6d6')
    a.image= photo
    a.place(x=650, y=957) 


# ...................attach-icon.........................

    attachicon= Image.open('D://TRELLA/Images/attach.png')
    photo = ImageTk.PhotoImage(attachicon)
    attach=tk. Button(reminder, 
                          image=photo,
                          bg='#d6d6d6',
                          bd=0,
                          cursor='hand2',
                          activebackground='#d6d6d6')
    attach.image= photo
    attach.place(x=720, y=960) 
    
# ...................insert-icon.........................

    inserticon= Image.open('D://TRELLA/Images/insert.png')
    photo = ImageTk.PhotoImage(inserticon)
    insert=tk. Button(reminder, 
                          image=photo,
                          bg='#d6d6d6',
                          bd=0,
                          cursor='hand2',
                          activebackground='#d6d6d6')
    insert.image= photo
    insert.place(x=790, y=962) 

# ...................emoji-icon.........................

    emojiicon= Image.open('D://TRELLA/Images/emoji.png')
    photo = ImageTk.PhotoImage(emojiicon)
    emoji=tk. Button(reminder, 
                          image=photo,
                          bg='#d6d6d6',
                          bd=0,
                          cursor='hand2',
                          activebackground='#d6d6d6')
    emoji.image= photo
    emoji.place(x=860, y=960) 
# ...................drive-icon.........................


    driveicon= Image.open('D://TRELLA/Images/drive.png')
    photo = ImageTk.PhotoImage(driveicon)
    drive=tk. Button(reminder, 
                          image=photo,
                          bg='#d6d6d6',
                          bd=0,
                          cursor='hand2',
                          activebackground='#d6d6d6')
    drive.image= photo
    drive.place(x=930, y=960) 
# ...................gallery-icon.........................

    galleryicon= Image.open('D://TRELLA/Images/gallery.png')
    photo = ImageTk.PhotoImage(galleryicon)
    gallery=tk. Button(reminder, 
                          image=photo,
                          bg='#d6d6d6',
                          bd=0,
                          cursor='hand2',
                          activebackground='#d6d6d6')
    gallery.image= photo
    gallery.place(x=1000, y=960) 


# ...................lock-icon.........................

    lockicon= Image.open('D://TRELLA/Images/lock.png')
    photo = ImageTk.PhotoImage(lockicon)
    lock=tk. Button(reminder, 
                          image=photo,
                          bg='#d6d6d6',
                          bd=0,
                          cursor='hand2',
                          activebackground='#d6d6d6')
    lock.image= photo
    lock.place(x=1080, y=960) 
    
# ...................more-icon.........................

    moreicon= Image.open('D://TRELLA/Images/more.png')
    photo = ImageTk.PhotoImage(moreicon)
    more=tk. Button(reminder, 
                          image=photo,
                          bg='#d6d6d6',
                          bd=0,
                          cursor='hand2',
                          activebackground='#d6d6d6')
    more.image= photo
    more.place(x=1140, y=960) 
# ...................delete-icon.........................


    deleteicon= Image.open('D://TRELLA/Images/delete.png')
    photo = ImageTk.PhotoImage(deleteicon)
    delete=tk. Button(reminder, 
                          image=photo,
                          bg='#d6d6d6',
                          bd=0,
                          cursor='hand2',
                          activebackground='#d6d6d6')
    delete.image= photo
    delete.place(x=1830, y=960) 
    








dashboard()
reminder.mainloop()