import sqlite3

conn = sqlite3.connect('korea.db')

cur = conn.cursor()
#
#
# cur.execute('create table sample(no INTEGER, name TEXT, tel TEXT)')

# cur.execute('INSERT INTO sample VALUES(1,"python","010-123-4567")')
#
#
cur.execute('select * from sample')
#
print(cur.fetchone())








