import sqlite3 as lit

db = lit.connect('myemployee.db')

with db:

    newname = "updated name"
    user_id = 4

    cur = db.cursor()
    cur.execute('UPDATE users SET name = ? WHERE id = ?', (newname, user_id))
    db.commit()
    print("Data Updated Successfully")
