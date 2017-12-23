import sqlite3

def update_b():

    conn = sqlite3.connect('testdb.db')

    cur = conn.cursor()

    up_sql = 'update test set title=? where title=?'

    cur.execute(up_sql, ('중국사','한국사'))

    conn.commit()

    conn.close()


update_b()