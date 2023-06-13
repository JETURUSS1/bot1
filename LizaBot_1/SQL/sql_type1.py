def sql_table():
    import sqlite3 as sq

    with sq.connect("bot.db") as con:
        cur = con.cursor() #курсор

        cur.execute("""CREATE TABLE IF NOT EXISTS users (
        name TEXT,
        sex TEXT,
        old TEXT
        )""")





con.close()