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
                    VALUES("�ڽ���","010-1234-1234","shinhy@naver.com")""")

id = cursor.lastrowid # ���������� �߰��ǰų� ����� ���ڵ��� ��ȣ

print(id)