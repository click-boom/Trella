from tkinter import*
from PIL import ImageTk,Image


window=Tk()
window.title("Trella".center(400))
window.geometry("800x900")
# window.state("zoomed")
window.resizable(0,0)


bg1=Image.open("opppp.jpeg")
resiz_bg=bg1.resize((1280,890),Image.ANTIALIAS)
new_bg1=ImageTk.PhotoImage(image=resiz_bg)
img=Label(window,image=new_bg1)
img.place(x=0,y=0)

frame=Frame(window,bg="#F5F5F5")
frame.place(x=430,y=190,width=540,height=410)

lo1=Image.open("llogo.png")
res=lo1.resize((250,228),Image.ANTIALIAS)
new_lo1=ImageTk.PhotoImage(image=res)
newlbl=Label(frame,image=new_lo1,background="#F5F5F5")
newlbl.place(x=150,y=13)

gree=Label(frame,text="Welcome To Trella",font="Arial 17",fg="Royal blue",background="#F5F5F5")
gree.place(x=170,y=170)

# def gayab():
#     if userentry.get()=="username/Email":
#         userentry.delete(0,END)
def hide():
    but_neweye2.config("new_eye1")
    pasentry.config(show="*")

userentry=Entry(frame,width=27,font="Arial 11",fg="grey",bd=0)
userentry.place(x=160,y=220)

userentry.insert(0,"Username/Email",)

pasentry=Entry(frame,width=27,font="Arial 11",fg="grey",bd=0)
pasentry.place(x=160,y=270)

pasentry.insert(0,"Password")

eye1=Image.open("closed eye.png")
ress=eye1.resize((20,20),Image.ANTIALIAS)
new_eye1=ImageTk.PhotoImage(image=ress)

lnew_eye=Label(frame,image=new_eye1,background="#F5F5F5")

but_neweye1=Button(frame,image=new_eye1,bd=0,activebackground="white",background="white",command=hide)
but_neweye1.place(x=385,y=270)

eye2=Image.open("openeye.png")
reas=eye2.resize((20,20),Image.ANTIALIAS)
new_eye2=ImageTk.PhotoImage(image=reas)

lnew_eye2=Label(frame,image=new_eye2,background="white")

but_neweye2=Button(frame,image=new_eye2,bd=0,activebackground="white",background="#F5F5F5")
but_neweye2.place(x=385,y=270)

forgot=Button(frame,text="Forgot Password ?",
                                bd=0,
                                activebackground="#F5F5F5",
                                background="white",
                                font="Arial 9",
                                fg="Blue")
forgot.place(x=217,y=330)

log_in=Button(frame,text="Login",
                                bd=0,
                                activebackground="blue",
                                background="#F5F5F5",
                                font='open 11',
                                fg="white",
                                width=10,
                                )
log_in.place(x=350,y=300)

dontacc=Button(frame,text="Don`t have an account ?",
                                bd=0,
                                activebackground="white",
                                background="white",
                                font='open 11',
                                fg="grey",)
dontacc.place(x=200,y=360)













window.mainloop()
