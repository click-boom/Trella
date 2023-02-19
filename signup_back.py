import sqlite3
import os 
from datetime import datetime

def registered_table():
    if os.path.exists("reg_usrs.db"):

        conn = sqlite3.connect("reg_usrs.db")  
        c=conn.cursor()

    else:
    
        conn = sqlite3.connect("reg_usrs.db")    
        c=conn.cursor()
       
    # Creating Users Table
        c.execute(""" CREATE TABLE users(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT(10),
            email TEXT(30) UNIQUE , 
            epassword TEXT(10),
            cpassword TEXT(10)
        )""")
    
    #Creating Tasks table
        c.execute(""" CREATE TABLE reminder_table(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT(10),
            description TEXT(300),
            deploy_date DATETIME,
            deploy_time DATETIME,
            date_time DATETIME,
            is_repeat TINYINT,
            belongs_to INTEGER,
            CONSTRAINT fk_users
                FOREIGN KEY (belongs_to)
                REFERENCES users(id)
        )""")
        
    #Creating Notes table
        c.execute(""" CREATE TABLE notes_table(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT(10) UNIQUE,
            note TEXT(300),
            belongs_to INTEGER,
            CONSTRAINT fk_users
                FOREIGN KEY (belongs_to)
                REFERENCES users(id)
        )""")

    #Creating Checklist table
        c.execute(""" CREATE TABLE checklist_table(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT(10),
            items TEXT(60),
            belongs_to INTEGER,
            CONSTRAINT fk_users
                FOREIGN KEY (belongs_to)
                REFERENCES users(id)
        )""")
    conn.commit()
    conn.close()


def ins_into_users(w, x, y, z):
    conn = sqlite3.connect("reg_usrs.db")  
    c=conn.cursor()
    with conn:
        c.execute("INSERT INTO users(username,email,epassword,cpassword) VALUES (?, ?, ?, ?)",[w ,x, y, z])
    conn.commit()
    conn.close()

def ins_into_chk( x, y, z):
    conn = sqlite3.connect("reg_usrs.db")  
    c=conn.cursor()
    with conn:
        c.execute("INSERT INTO checklist_table(title, items, belongs_to) VALUES (?, ?, ?)",[x,y,z])    
    conn.commit()
    conn.close()

def ins_into_rem(t, u, v, w, x, y, z):
    conn = sqlite3.connect("reg_usrs.db")  
    c=conn.cursor()
    with conn:
        c.execute("INSERT INTO reminder_table(title, description, deploy_date, deploy_time, date_time, is_repeat, belongs_to) VALUES (?, ?, ?, ?, ?, ?, ?)",[t, u, v, w, x, y,z])    
    conn.commit()
    conn.close()

def ins_into_note(x, y, z):
    conn = sqlite3.connect("reg_usrs.db")  
    c=conn.cursor()
    with conn:
        c.execute("INSERT INTO notes_table(title, note, belongs_to) VALUES (?, ?, ?)",[x,y,z])    
    conn.commit()
    conn.close()

registered_table()

   
 # c.execute("DELETE FROM users")


def dell_usrs(uid:int):
    conn = sqlite3.connect("reg_usrs.db")  
    c=conn.cursor()
    c.execute("DELETE FROM users WHERE ID=?",[uid])
    conn.commit()

def dell_chk(id:int):
    conn = sqlite3.connect("reg_usrs.db")  
    c=conn.cursor()
    c.execute("DELETE FROM checklist_table WHERE belongs_to=?",[id])
    conn.commit()

def dell_rem(id:int):
    conn = sqlite3.connect("reg_usrs.db")  
    c=conn.cursor()
    c.execute("DELETE FROM reminder_table WHERE belongs_to=?",[id])
    conn.commit()

def dell_note(id:int):
    conn = sqlite3.connect("reg_usrs.db")  
    c=conn.cursor()
    c.execute("DELETE FROM notes_table WHERE belongs_to=?",[id])
    conn.commit()

def get_usr_info(user_id:int)->list:
    conn = sqlite3.connect("reg_usrs.db")  
    c=conn.cursor()
    with conn:
         c.execute("SELECT * FROM users where ID=?",[user_id])
         data=c.fetchall()
         print(data)

def get_rem_tasks_of_user(user_id:int)->list:
    conn = sqlite3.connect("reg_usrs.db")  
    c=conn.cursor()
    with conn:
        data = c.execute("SELECT * FROM reminder_table where belongs_to=?",[user_id])
        for task in data:
            print(task)

def get_note_tasks_of_user(user_id:int,title)->list:
    conn = sqlite3.connect("reg_usrs.db")  
    c=conn.cursor()
    with conn:
        c.execute("SELECT note FROM notes_table where belongs_to=? AND title=?",[user_id, title])
        data=c.fetchall()
        print(data)


# dell_usrs(6)
# dell_rem(5)
# get_rem_tasks_of_user(1)
# get_usr_info(2)

# ins_into_note('Rohan', 'Watch Re/Member', '2')
# get_note_tasks_of_user(2, 'Rohan')

""" Insert into users 1st values """
# ins_into_users('Rohan', 'roahhanchaulagain@gmail.com', 'rhsn123', 'rhsn123')
# ins_into_users('Haseena', 'rkc697418@gmail.com', 'hrsn123', 'hrsn123')
# ins_into_users('Sujina', 'sujinasht307@gmail.com', 'snrh123', 'snrh123')
# ins_into_users('Nikesh', 'bhandarinikesh93@gmail.com', 'nsrh123', 'nsrh123')
# ins_into_users('Ashutosh', 'ashboy@gmail.com', 'bhadre', 'bhadre')

ins_into_rem('Rohan', 'Wakeup', '2023-02-19', '8:40 AM', '2023-02-19 8:50:00',0,5)

# dell_rem(5)
