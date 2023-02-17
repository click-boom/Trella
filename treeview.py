import tkinter as tk
from tkinter import ttk

window=tk.Tk()
window.title('TRELLA')
window.geometry('1920x1080')
window.minsize(1920, 1080)

treee=ttk.Treeview(window)

treee['columns']=('ID','Description','Deploy date', 'Deploy time', 'Repeat','Rep')

treee.column("#0",width=120,minwidth=40)
treee.column("ID",width=120,minwidth=20)
treee.column("Description",width=120,minwidth=55)
treee.column("Deploy date",width=120,minwidth=45)
treee.column("Deploy time",width=120,minwidth=55)
treee.column("Repeat",width=120,minwidth=40)
treee.column("Rep",width=120,minwidth=55)

treee.heading("#0",text="S.N",anchor=tk.W)
treee.heading("ID",text="ID",anchor=tk.W)
treee.heading("Description",text="Description",anchor=tk.W)
treee.heading("Deploy date",text="Deploy date",anchor=tk.W)
treee.heading("Deploy time",text="Deploy time",anchor=tk.W)
treee.heading("Repeat",text="Repeat",anchor=tk.W)
treee.heading("Rep",text="Rep",anchor=tk.W)

xscrollbar = ttk.Scrollbar(window, orient="horizontal", command=treee.xview)
treee.configure(xscrollcommand=xscrollbar.set)
xscrollbar.pack(side="bottom", fill="x")

yscrollbar = ttk.Scrollbar(window, orient="vertical", command=treee.yview)
treee.configure(yscrollcommand=yscrollbar.set)
yscrollbar.pack(side="right", fill="y")

canvas = tk.Canvas(window, bg='white', height=900, width=1600)
canvas.pack(fill='both', expand=True)

treee.pack()

xscrollbar.pack(side='bottom', fill='x')
yscrollbar.pack(side='right', fill='y')

treee.configure(xscrollcommand=xscrollbar.set, yscrollcommand=yscrollbar.set)
xscrollbar.config(command=treee.xview)
yscrollbar.config(command=treee.yview)

canvas.create_window((0,0), window=treee, anchor='nw')

treee.pack()

window.mainloop()
