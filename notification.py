import notify2
import sqlite3
from datetime import datetime
import time
from playsound import playsound

def gen_rem():
    
    notify2.init("My Application")
    def reminder(x, y):
        notification = notify2.Notification(x, y)
        notification.icon('/home/wae/Documents/giri raj sir/Trella/Images/llogo.png')
        notification.show()
        
    format = '%Y-%m-%d %H:%M:%S'
    conn=sqlite3.connect('reg_usrs.db')
    c=conn.cursor()

    c.execute("SELECT title, description, date_time FROM reminder_table WHERE belongs_to=?",[1])
    rows = c.fetchall()
    for i in range(len(rows)):
        datetime_str=str(rows[i][2])
        dt= datetime.strptime(datetime_str, format)
        reminder_time = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        delay = (reminder_time - datetime.now()).total_seconds()
        try:
            time.sleep(delay)
            reminder(rows[i][0], rows[i][1])
            playsound('/home/wae/Documents/giri raj sir/Trella/sound.wav')
        except:
            pass
gen_rem()
