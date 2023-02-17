import tkinter as tk

down_frame=tk.Tk()
down_frame.title("To-Do-list")
down_frame.geometry("400x650+400+100")
down_frame.resizable(False,False)

def on_press(str):
    add.delete(0, tk.END)

def on_unpress(str):
    add.delete(0, tk.END)
    if add.get()=='':
        add.insert(0,'Reminder Description...')


def on_press_add(str):
    title.delete(0, tk.END)

def on_unpress_add(str):
    title.delete(0, tk.END)
    if title.get()=='':
        title.insert(0,'Reminder Title...')


# tentry_var=tk.StringVar()
title=tk.Entry(down_frame, font=('yu gothic ui', 20, 'bold'), bd=0 ,highlightthickness=0, width=15)
title.place(x=70,y=15)
title.insert(0,'Reminder Title....')
title.bind("<FocusIn>",on_press_add)
title.bind("FocusOut",on_unpress_add)
    
# dentry_var=tk.StringVar()
add=tk.Entry(down_frame, font=('yu gothic ui', 20, 'bold'), bd=0 ,highlightthickness=0, width=20)
add.place(x=20,y=78)
add.insert(0,'Reminder Description....')
add.bind("<FocusIn>",on_press)
add.bind("<FocusOut>",on_unpress)


down_frame.mainloop()

