import sqlite3

conn = sqlite3.connect('student.db')

sql = '''
    CREATE TABLE student
        (
            name text,
            no   integer,
            addr text
        )
'''

c = conn.cursor()

c.execute(sql)

c.close()

conn.commit()


