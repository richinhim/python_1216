#coding: euc-kr

import  sqlite3

db =sqlite3.connect('testdb.db')

cursor = db.cursor()

#
# cursor.execute(""" CREATE TABLE PHONEBOOK(NAME text,
#                     PHONE text, EMAIL text)
#                     """)
#
# db.commit()

cursor.execute(""" INSERT INTO PHONEBOOK(NAME,
                    PHONE, EMAIL)
                    VALUES("박신혜","010-1234-1234","shinhy@naver.com")""")

id = cursor.lastrowid # 마지막으로 추가되거나 변경된 레코드의 번호

print(id)