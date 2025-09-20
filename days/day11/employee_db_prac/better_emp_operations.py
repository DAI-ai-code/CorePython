import pymysql

from days.day11.employee_db_prac.emp_db_class import Employee

con = pymysql.connect(host="localhost", user="root", password="112233", database="emp_db", autocommit=True)
cursor = con.cursor()

def inserter(eid,name,salary):
    cursor.execute("insert into employee values({},'{}',{})".format(eid,name,salary))
    

def deleter(eid):
    cursor.execute(f"delete from employee where id={eid}")
    

def updater(eid, name, salary):
    cursor.execute(f"update employee set name='{name}' where id={eid}")
    

def selector(eid, name, salary):
    cursor.execute(f"select * from employee where salary>{salary}")
    data = cursor.fetchall()
    print(data)
    

def select_all():
    cursor.execute(f"select * from employee")
    data = cursor.fetchall()
    print(data)


e1 = Employee(1,"abc",99000)
e2 = Employee(2,"bcd", 89000)
e3 = Employee(3,"cde",90000)
e4 = Employee(4,"def", 100000)

e = [e1,e2,e3,e4]
# for emp in e:
#     inserter(emp.empid, emp.ename, emp.esalary)

select_all()
selector(1,"a",90000)


