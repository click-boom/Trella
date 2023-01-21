import sqlite3
from signup import sign_up
conn=sqlite3.connect("reg_usrs.db")
c=conn.cursor()


# Creating Table
# c.execute(""" CREATE TABLE users(
#     username text(10),
#     email text(30),
#     epassword text(10),
#     cpassword text(10)
# )""")

conn.close()