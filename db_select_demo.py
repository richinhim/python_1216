import sqlite3

conn = sqlite3.connect('testdb.db')

curs = conn.cursor()
for row in curs.execute('SELECT * from test'):
    print(row)


curs.execute('SELECT * from test')

while(True):

    row = curs.fetchone()

    if(row == None):
        break
    name, count = row

    print(name, count)

curs.close()

conn.commit()

