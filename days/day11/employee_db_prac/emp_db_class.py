class Employee:
    count = 0

    def __init__(self, empid, ename, esalary):
        Employee.count += 1
        self.empid = empid
        self.ename = ename
        self.esalary = esalary


    def show_deets(self):
        print(f'Employer ID: {self.empid}\nname:{self.ename}\nSalary : {self.esalary}')

    def __repr__(self):
        return f"empid='{self.empid}','name={self.ename}', esalary={self.esalary})"

    def __gt__(self, other):
        return self.esalary < other.esalary

    @staticmethod
    def print_count():
        print(f'count = {Employee.count}')


