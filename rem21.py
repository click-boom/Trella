import tkinter as tk
from tkinter import messagebox, filedialog
import datetime

def save_note():
    note = text_widget.get("1.0", "end-1c")
    with open("notes.txt", "a") as f:
        f.write(f"{datetime.datetime.now()}: {note}\n")
    text_widget.delete("1.0", "end")
    messagebox.showinfo("MY Notes", "Note saved!")
    load_notes()

def set_reminder():
    reminder_time = reminder_entry.get()
    reminder_text = reminder_text_widget.get("1.0", "end-1c")
    with open("reminders.txt", "a") as f:
        f.write(f"{reminder_time}: {reminder_text}\n")
    reminder_entry.delete(0, "end")
    reminder_text_widget.delete("1.0", "end")
    messagebox.showinfo("MY Notes", "Reminder set!")
    load_reminders()

def load_notes():
    with open("notes.txt", "r") as f:
        notes_list.delete(0, "end")
        for line in f:
            notes_list.insert("end", line)

def load_reminders():
    with open("reminders.txt", "r") as f:
        reminders_list.delete(0, "end")
        for line in f:
            reminders_list.insert("end", line)

def delete_note():
    selected_note = notes_list.get(notes_list.curselection())
    with open("notes.txt", "r") as f:
        lines = f.readlines()
    with open("notes.txt", "w") as f:
        for line in lines:
            if line != selected_note:
                f.write(line)
    load_notes()
    messagebox.showinfo("MY Notes", "Note deleted!")

def delete_reminder():
    selected_reminder = reminders_list.get(reminders_list.curselection())
    with open("reminders.txt", "r") as f:
        lines = f.readlines()
    with open("reminders.txt", "w") as f:
        for line in lines:
            if line != selected_reminder:
                f.write(line)
    load_reminders()
    messagebox.showinfo("MY Notes", "Reminder deleted!")

root = tk.Tk()
root.title("MY Notes")

# Note taking
text_widget = tk.Text(root, height=10, width=40)
text_widget.pack()

save_button = tk.Button(root, text="Save Note", command=save_note)
save_button.pack()

# Notes list
notes_frame = tk.Frame(root)
notes_frame.pack()

notes_list = tk.Listbox(notes_frame)
notes_list.pack()

delete_note_button = tk.Button(notes_frame, text="Delete Note", command=delete_note)
delete_note_button.pack()

load_notes()

# Reminder setting
reminder_frame = tk.Frame(root)
reminder_frame.pack()

reminder_entry = tk.Entry(reminder_frame)
reminder_entry.pack(side="left")

reminder_text_widget = tk.Text(reminder_frame, height=5, width=30)
reminder_text_widget.pack(side="right")

set_reminder_button = tk.Button(root, text="Set Reminder", command=set_reminder)
set_reminder_button.pack()

# Reminders list
reminders_frame = tk.Frame(root)
reminders_frame.pack()

reminders_list = tk.Listbox(reminders_frame)
reminders_list.pack()

delete_reminder_button = tk.Button(reminders_frame, text="Delete Reminder", command=delete_reminder)
delete_reminder_button.pack()

load_reminders()

root.mainloop()
