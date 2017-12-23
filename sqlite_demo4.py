import sqlite3

conn = sqlite3.connect(':memory:')

sql = """
	CREATE TABLE product
	(
		commodity text,
		product   text,
		amount   integer,
		date      DATE
	)
"""
conn.execute(sql)

conn.commit()

statement = '''
	INSERT INTO product VALUES
		(?,?,?,?)
'''

data = [
	('02', '수박', 20, '2017-12-23'),
	('03', '수박', 50, '2017-12-23'),
	('04', '수박', 70, '2017-12-23')
]

conn.executemany(statement, data)

conn.commit()

cursor = conn.execute('select * from product')

rows = cursor.fetchall()

row_counter = 0

for row in rows:
	print(row)
	row_counter = row_counter + 1

print('Number of rows: {}'.format(row_counter))
