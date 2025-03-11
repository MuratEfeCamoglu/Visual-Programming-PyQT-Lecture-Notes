import sqlite3 as lit

def main():
    try:
       db = lit.connect('./yedincihafta/PyQt5-SqLite-Crud-Project/myemployee.db')
       print("Database created")
    except:
        print("failed to create database")
    finally:
        db.close()

if __name__ == "__main__":
    main()