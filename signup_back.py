import sqlite3

conn = sqlite3.connect("reg_usrs.db")
c=conn.cursor()
# Creating Table
# c.execute(""" CREATE TABLE users(
#     username text(10),
#     email text(30),
#     epassword text(10),
#     cpassword text(10)
# )""")


def ins(w, x, y, z):
    with conn:
        c.execute("INSERT INTO users VALUES (:username,:email, :epassword, :cpassword)",{'username':w, 'email':x,  'epassword':y,  'cpassword':z})

# ins('', 'rubyrose7@gmail.com', 'rubyruby', 'rubyruby')

c.execute("DELETE FROM users WHERE email='rubyrose7@gmail.com'")
conn.commit()
conn.close()