import tkinter
from tkinter import*
root=Tk()
root.title("To-Do-list")
root.geometry("400x650+400+100")
root.resizable(False,False)

task_list=[]

def openTaskfile():
    try:
        with open("tasklist.txt","r") as taskfile:
            tasks=taskfile.readlines()
        for task in tasks:
            if task!='/n':
                task_list.append(task)
                listbox.insert(END,task)

    except:
        file=open('tasklist.txt','w')
        file.close()


heading=Label(root,text="all task",font="Arial 20 bold",fg="white",bg="#32405b")
heading.place(x=130,y=20)

frame=Frame(root,width=400,height=50,bg="white")
frame.place(x=0,y=180)

task=StringVar()
task_entry=Entry(frame,width=18,font="arial 20",bd=0)
task_entry.place(x=10,y=7)

button=Button(frame,text="ADD",font="arial 20",width=6,bg="#5a95ff",fg="#fff",bd=0)
button.place(x=200,y=0)

frame1=Frame(root,bd=3,width=700,height=280,bg="#32405b")
frame1.pack(pady=(160,0))

listbox=Listbox(frame1,font=("arial 12"),width=40,height=16,bg="#32405b",fg="White",cursor="hand2",selectbackground="#5a95ff")
listbox.pack(side=RIGHT,fill=BOTH,padx=2)

scrollbar=Scrollbar(frame1)
scrollbar.pack(side=RIGHT,fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

delete_icon=Button(frame1,text="Delete",font="arial 20",width=6,bg="#5a95ff",fg="#fff",bd=0)
delete_icon.place(x=100,y=200)
root.mainloop()