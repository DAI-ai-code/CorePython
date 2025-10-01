import pymysql

from days.day11.employee_db_prac.emp_db_class import Employee

con = pymysql.connect(host="localhost", user="root", password="112233", database="emp_db", autocommit=True)
cursor = con.cursor()


def inserter(employee:Employee):
    cursor.execute("insert into employee values({},'{}',{})".format(employee.empid, employee.ename, employee.esalary))
    select_all()


def deleter(employee:Employee):
    cursor.execute(f"delete from employee where id={employee.empid}")
    select_all()


def updater(employee:Employee, name):
    cursor.execute(f"update employee set name='{name}' where id={employee.empid}")
    select_all()


def selector(eid, name, salary):
    cursor.execute(f"select * from employee where salary>{salary}")
    data = cursor.fetchall()
    print(data)


def select_all():
    cursor.execute(f"select * from employee")
    data = cursor.fetchall()
    return data



