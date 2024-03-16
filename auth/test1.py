import sqlite3 as sq



with sq.connect("db.sqlite3") as con_db:
            cur_db = con_db.cursor()
            
            cur_db.execute("select * from games")
            result = cur_db.fetchall()
            print(result)