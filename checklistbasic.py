import tkinter as tk

def add_label():
    text = entry_box.get()

    label = tk.Label(frame, text=text, bg='lightblue')
    label.pack()
    entry_box.delete(0, 'end')

def delete_label():
    text = entry_box.get()
    for widget in frame.winfo_children():
        if isinstance(widget, tk.Label) and widget['text'] == text:
            widget.destroy()
    # Clear the text from the entry box
    entry_box.delete(0, 'end')

def update_label():
    new_text = entry_box.get()
    for widget in frame.winfo_children():
        if isinstance(widget, tk.Label):
            widget['text'] = new_text

root = tk.Tk()
root.geometry('800x700')

frame = tk.Frame(root, bg='lightblue')
frame.pack(fill='both', expand=True)

entry_box = tk.Entry(frame)
entry_box.pack(pady=10)


add_button = tk.Button(frame, text="Add", command=add_label)
add_button.pack(side='left', padx=10)
delete_button = tk.Button(frame, text="Delete", command=delete_label)
delete_button.pack(side='left', padx=10)

update_button = tk.Button(frame, text="Update", command=update_label)
update_button.pack(side='left', padx=10)

root.mainloop()

