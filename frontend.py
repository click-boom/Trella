from tkinter import*
from PIL import ImageTk,Image
window_trela=Tk()
window_trela.title("Sign Up")
window_trela.geometry("870x870+250+250")
# window_trela.configure(bg="#FFFDF8")
window_trela.resizable(True,True)

# the image of logo is too big so we are croping our image /resize the image
#opening the image 
image_logo=Image.open("newlogo.png")

# resixed the image
resized=image_logo.resize((200,200),Image.ANTIALIAS)

new_image_logo=ImageTk.PhotoImage(resized)
#image size 
my_lable=Label(window_trela,image=new_image_logo)
my_lable.place(x=520,y=90)

#welcomming bar 
font_greating=Label(window_trela,text="Welcome to TRELA",font="Times 20 bold",fg="#0A49DB").place(x=480,y=270)


Usename=Label(window_trela,text="Username")
Usename.place(x=480,y=325)
# use name  and password entry
username_entry=Entry(window_trela,width=35, font=("Times 10 bold"),bd=0,fg="#0A49DB" )
username_entry.place(x=480,y=350)

password=Label(window_trela,text="Password")
password.place(x=480,y=377)

password_entry=Entry(window_trela,width=35, font=("Times 10 bold"),bd=0,fg="#808080")
password_entry.place(x=480,y=400) 

    
    
















window_trela.mainloop()
