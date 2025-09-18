class Employee:
    def __init__(self, empid, ename, salary):
        self.empid = empid
        self.ename = ename
        self.salary = salary

    def printer(self):
        print(f'empid : {self.empid} name : {self.ename} salary : {self.salary}')

class Manager(Employee):
    def __init__(self, empid, ename, salary, rating):
        self.rating = rating
        super().__init__(empid, ename, salary)

    def printer(self):
        print(str(super().printer()) + f'salary : {self.salary}')


e = Employee(1, 'e1', 10)
e.printer()
m = Manager(2, 'm1', 30, 3.4)
m.printer()