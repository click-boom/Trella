from tkinter import*
from PIL import Image,ImageTk
window=Tk()

#........................defining window....................
def dashboard():
    window.title('Trella')
    window.geometry('1920x1080')
    window.state("zoomed")
    window.config(background="#6c6c6c")

#..............................window icon...............
    trella_icon=PhotoImage(file='D:/trela/llogo.png')
    window.iconphoto(True,trella_icon)


#..........logout button..........
    btn_logout=PhotoImage(file="D:/trela/Buttonlogout.png")
    dash_logout_btn=Label(window,image=btn_logout,background="#6c6c6c")
    dash_logout_btn.image=btn_logout
    dash_logout_btn.place(x=500,y=600)

    logout_dash=Button(dash_logout_btn,text="Log Out",
                        font=('yu gothic ui',18,'bold'),
                        width=10,
                        bd=0,
                        highlightthickness=0,
                        cursor='hand2',
                        activebackground="#a4a4a4",
                        fg="red"
                        )
    logout_dash.place(x=15,y=690)
    

#..........................Header................................

    
    Head_er=Frame(window,bg="#748AC1")
    Head_er.place(x=350 , y=0,width=1590,height=80)

#..........................sidebar ................................
    side_bar=Frame(window,bg="#DFEAF6")
    side_bar.place(x=0,y=0,width=360,height=1100)

    starting_logo=PhotoImage(file="D:/trela/llogo.png")
    starting_logo_lable=Label(window,image=starting_logo,background="#DFEAF6")
    starting_logo_lable.image=starting_logo
    starting_logo_lable.place(x=100,y=44)

#................greatings..........................................






    










dashboard()
window.mainloop()