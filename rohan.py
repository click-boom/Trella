import tkinter as tk
root=tk.Tk()

root.title("Sign up")
root.geometry('1024x720+300+300')
root.resizable()

logo=tk.PhotoImage(file='/home/wae/Documents/giri raj sir/Trella/dlogo.png')
img_area=tk.Label(root,
                    compound=tk.TOP,
                    image=logo,
                    text='Welcome To Trella',
                    font="Times 20 bold",
                    fg="#0A49DB").pack()

usr_pwd=tk.LabelFrame(root)
Usename=tk.Label(usr_pwd,text="Username").place(x=480,y=325)
username_entry=tk.Entry(usr_pwd,width=35, font=("Times 10 bold"),bd=0,fg="#0A49DB" ).place(x=480,y=350)

password=tk.Label(usr_pwd,text="Password").place(x=480,y=377)
password_entry=tk.Entry(usr_pwd,width=35, font=("Times 10 bold"),bd=0,fg="#808080").place(x=480,y=400) 

print("hekkk")

root.mainloop()
