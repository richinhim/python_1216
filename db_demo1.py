#coding:euc-kr
import sqlite3
#
def select_b():

    conn = sqlite3.connect("testdb.db")

    cur = conn.cursor()

    cur.execute('select * from test')

    print('[1] 전체 데이터 출력하기')

    rs = cur.fetchall()

    for book in rs :
        print(book)

    conn.close()
#
if __name__ == "__main__":
    select_b()