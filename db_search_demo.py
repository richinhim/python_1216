#coding:euc-kr

import sqlite3

db = sqlite3.connect('testdb.db')

cursor = db.cursor()

cursor.execute("SELECT * from PHONEBOOK")

rows = cursor.fetchone()

print(rows)

cursor.close()


cursor = db.cursor()

cursor.execute("SELECT * from PHONEBOOK")

rows = cursor.fetchall()

print(rows)

cursor.close()

db.close()