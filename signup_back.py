import sqlite3

conn = sqlite3.connect("reg_usrs.db")
c=conn.cursor()
# Creating Table
# c.execute(""" CREATE TABLE users(
#     username text(10) PRIMARY KEY,
#     email text(30) UNIQUE , 
#     epassword text(10),
#     cpassword text(10)
# )""")


def ins(w, x, y, z):
    with conn:
        c.execute("INSERT INTO users VALUES (?, ?, ?, ?)",[w ,x, y, z])

# ins('Rohan', 'roahhanchaulagain@gmail.com', 'rhsn123', 'rhsn123')
# ins('Ashutosh', 'ashboy@gmail.com', 'bhadre', 'bhadre')

c.execute("DELETE FROM users WHERE email='sandy123@gmail.com'")
conn.commit()
conn.close()