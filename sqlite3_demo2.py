import sqlite3

conn = sqlite3.connect('student.db')

sql = '''
    INSERT INTO student VALUES
           (?,?,?)
'''

c = conn.cursor()

c.execute(sql, ('학생2', 2, '서울'))

# data 형태는 리스트 아니면 튜플만 가능하다.
data = [
    ('학생3', 3, '강원'),
    ('학생4', 4, '경기'),
    ('학생5', 5, '충청')
]

c.executemany(sql, data)

c.execute('select * from student')

print(c.fetchall())


c.close()
conn.commit()

