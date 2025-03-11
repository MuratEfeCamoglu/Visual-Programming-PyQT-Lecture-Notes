import sqlite3 as lit
myuser = (

    (1, 'Parwiz', 'par@gmail.com'),
    (2, 'John', 'john@gmail.com'),
    (3, 'Bob', 'bob@gmail.com'),
    (4, 'Tom', 'tom@gmail.com'),

)
db = lit.connect('myemployee.db')

with db:
    cur = db.cursor()
    cur.executemany('INSERT INTO users VALUES (?,?,?)', myuser)

    print("Data Inserted Successfully")