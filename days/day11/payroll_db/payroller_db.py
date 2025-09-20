import pymysql

from days.day10.payrollexceptions.InvalidMedicalAllowanceError import MedicalAllowanceError

from days.day10.payrollexceptions.Travel import LessTravelledError


class Employee:
    table_counter = 0
    def __init__(self, empid, ename, basic_salary, medical_allowance):
        self.empid = empid
        self.ename = ename
        self.basic_salary = basic_salary
        self.pf = self.basic_salary*0.12
        self.pt = 200
        self.hra = self.basic_salary*0.5
        self.medical_allowance = medical_allowance

        if self.medical_allowance < 2000:
            raise MedicalAllowanceError

    def calculate_salary(self):
        gross = self.pf + self.pt + self.hra + self.basic_salary
        net = gross - self.pf - self.pt

        return gross,net

    def show_details(self):
        print("ID: {}, Name: {}, Basic salary: {}, PF: {}, PT:{}, HRA: {}, Medical allowance: {}".format(self.empid,self.ename,self.basic_salary,self.pf, self.pt,self.hra,self.medical_allowance))

    def add_to_table(self):
        conn = pymysql.connect(host='localhost', user='root', password='112233', database='emp_db', autocommit=True)
        cursor = conn.cursor()
        if Employee.table_counter==0:
            cursor.execute("""
            CREATE TABLE employees (
                empid INT PRIMARY KEY,
                position varchar(200),
                name VARCHAR(100),
                salary INT,
                PF INT,
                PT INT,
                HRA INT,
                medical_allowance INT,
                manager_allowance INT,
                food_allowance INT,
                other_allowance INT,
                phone_allowance INT,
                travel_allowance INT
            )
            """)
            Employee.table_counter += 1
        parameters = (self.empid, "Employee", self.ename, self.basic_salary, self.pf, self.pt,
                      self.hra, self.medical_allowance, None, None,
                      None, None, None)
        cursor.execute(f"insert into employees values (%s, %s ,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", parameters)


class Manager(Employee):
    def __init__(self, empid, ename, basic_salary, medical_allowance):
        super().__init__(empid, ename, basic_salary, medical_allowance)
        self.manager_allowance, self.food_allowance, self.other_allowance = self.basic_salary*0.08, self.basic_salary*0.1, self.basic_salary*0.03

    def calculate_salary(self):
        gross = super().calculate_salary()[0] + self.manager_allowance + self.food_allowance + self.other_allowance
        net = gross - self.pf - self.pt
        return gross, net

    def show_details(self):
        print("ID: {}, Name: {}, Basic salary: {}, PF: {}, PT:{}, HRA: {}, Medical allowance: {}, Manager allowance: {}, Food allowance: {}, Other allowance: {}".format(self.empid,self.ename,self.basic_salary,self.pf, self.pt,self.hra,self.medical_allowance, self.manager_allowance, self.food_allowance, self.other_allowance))

    def add_to_table(self):
        conn = pymysql.connect(host='localhost', user='root', password='112233', database='emp_db', autocommit=True)
        cursor = conn.cursor()
        parameters = (self.empid, "Manager", self.ename, self.basic_salary, self.pf, self.pt,
                       self.hra, self.medical_allowance, self.manager_allowance, self.food_allowance, self.other_allowance, None, None)
        cursor.execute(f"insert into employees values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", parameters)

class MarketingExecutive(Employee):
    def __init__(self, empid, ename, basic_salary, medical_allowance, kms_travelled):
        super().__init__(empid, ename, basic_salary, medical_allowance)
        self.kms_travelled = kms_travelled
        self.phone_allowance = 1000
        self.travel_allowance = 5 *self.kms_travelled
        if self.kms_travelled < 1:
            raise LessTravelledError

    def calculate_salary(self):
        salaries = super().calculate_salary()
        gross = salaries[0] + self.phone_allowance + self.kms_travelled
        net = gross - self.pt - self.pf
        return gross, net

    def show_details(self):
        print(
            "ID: {}, Name: {}, Basic salary: {}, PF: {}, PT:{}, HRA: {}, Medical allowance: {}, Phone allowance: {}, Travel allowance: {}".format(
                self.empid, self.ename, self.basic_salary, self.pf, self.pt, self.hra, self.medical_allowance,
                self.phone_allowance, self.travel_allowance))

    def add_to_table(self):
        conn = pymysql.connect(host='localhost', user='root', password='112233', database='emp_db', autocommit=True)
        cursor = conn.cursor()
        parameters = (self.empid, "Marketing Executive", self.ename, self.basic_salary, self.pf, self.pt,
                      self.hra, self.medical_allowance, None, None,
                      None, self.phone_allowance, self.travel_allowance)
        cursor.execute(f"insert into employees values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", parameters)


emp1 = Employee(1,"AAA",10000,2000)
emp1.calculate_salary()
emp1.add_to_table()
# emp1.show_details()

man1 = Manager(2, "BBB", 20000, 2300)
man1.calculate_salary()
man1.add_to_table()
# man1.show_details()

marexe1 = MarketingExecutive(3, "CCC", 30000, 7500, 5)
marexe1.calculate_salary()
marexe1.add_to_table()
# marexe1.show_details()





