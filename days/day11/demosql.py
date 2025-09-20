import pymysql

conn = pymysql.connect(host='localhost', user='root', password='112233', database='mysqldemo')
cursor = conn.cursor()
# cursor.execute('create database mysqldemo')
cursor.execute('use mysqldemo')
cursor.execute('create table demostudent(rno int, name varchar(200), marks int)')
cursor.execute("select * from demostudent")
cursor.execute("insert into demostudent values(1, 'abc', 80)")
cursor.execute("insert into demostudent values(2, 'bbb', 70)")
cursor.execute("insert into demostudent values(3, 'ccc', 60)")
data = cursor.fetchall()
print(data)
cursor.execute("update demostudent set name='aaa' where rno=1")
cursor.execute("delete from demostudent where rno=3")
cursor.execute("select * from demostudent where marks>70")
cursor.execute("select * from demostudent")
data = cursor.fetchall()
print(data)
conn.commit()
conn.close()






