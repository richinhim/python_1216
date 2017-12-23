#coding:euc-kr
import sqlite3

def insert_table():
    conn = sqlite3.connect('testdb.db')

    cur = conn.cursor()

    data = [
        ('���ΰ��ٴ� ','����','�������ǻ�',20,20),
        ('�ѱ���', '����1', '�������ǻ�1', 20, 20)
    ]

    statement = '''
    	INSERT INTO test VALUES
    		(?,?,?,?,?)
    '''
    cur.executemany(statement, data)

    conn.commit()

if __name__ == "__main__":
    insert_table()

