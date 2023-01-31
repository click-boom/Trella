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
            username text(10),
            email text(30) UNIQUE , 
            epassword text(10),
            cpassword text(10)
        )""")
    
    #Creating Tasks table
        c.execute(""" CREATE TABLE reminder_table(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Description text(300),
            Deploy_time DATETIME,
            is_repeat TINYINT,
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


def ins_into_rem(w, x, y, z):
    conn = sqlite3.connect("reg_usrs.db")  
    c=conn.cursor()
    with conn:
        c.execute("INSERT INTO reminder_table(Description, Deploy_time, is_repeat, belongs_to) VALUES (?, ?, ?, ?)",[w,x,y,z])    
    conn.commit()
    conn.close()

registered_table()

   
 # c.execute("DELETE FROM users")

""" Insert into users 1st values """
# ins_into_users('Rohan', 'roahhanchaulagain@gmail.com', 'rhsn123', 'rhsn123')
# ins_into_users('Haseena', 'rkc697418@gmail.com', 'hrsn123', 'hrsn123')
# ins_into_users('Sujina', 'sujinasht307@gmail.com', 'snrh123', 'snrh123')
# ins_into_users('Nikesh', 'bhandarinikesh93@gmail.com', 'nsrh123', 'nsrh123')
# ins_into_users('Ashutosh', 'ashboy@gmail.com', 'bhadre', 'bhadre')

ins_into_rem('Eat food at 11', datetime.utcnow(), 'bhadre', 'bhadre')

# c.execute("DELETE FROM users WHERE ID=2")
