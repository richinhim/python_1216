import sqlite3
#
def create_table():
    conn = sqlite3.connect('testdb.db')

    cur = conn.cursor()

    sql = '''
        create table test(
            title text,
            pubd text,
            pus text,
            page integer,
            re integer
        )
    '''

    cur.execute(sql)

    conn.commit()

    conn.close()

    #

create_table()

