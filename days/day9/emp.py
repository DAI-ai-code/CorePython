class Employee:
    count = 0

    def __init__(self, empid, esalary):
        Employee.count += 1
        self.empid = empid
        self.esalary = esalary



    def show_deets(self):
        print(f'Employer ID: {self.empid}\nSalary : {self.esalary}')

    def __repr__(self):
        return f"Employee(empid='{self.empid}', esalary={self.esalary})"

    # def __lt__(self, other):
    #     return self.empid<other.empid

    def __gt__(self, other):
        return self.esalary < other.esalary

    @staticmethod
    def print_count():
        print(f'count = {Employee.count}')

e1 = Employee('1', 1000)
e2 = Employee('9', 2000)
e3 = Employee('3', 100)

print("------------")
emps = [e1,e2,e3]
emps.sort()
print(emps)
Employee.print_count()
