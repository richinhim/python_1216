#coding:euc-kr
import sqlite3

def insert_table():
    conn = sqlite3.connect('testdb.db')

    cur = conn.cursor()

    data = [
        ('노틀담의 꼽추','노인','노인출판사',20,20),
        ('한국사', '노인1', '노인출판사1', 20, 20)
    ]

    statement = '''
    	INSERT INTO test VALUES
    		(?,?,?,?,?)
    '''
    cur.executemany(statement, data)

    conn.commit()

insert_table()

