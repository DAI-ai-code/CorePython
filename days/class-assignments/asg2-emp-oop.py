class Employee:

    def __init__(self, empid, ename, basic_salary, medical_allowance):
        self.empid = empid
        self.ename = ename
        self.basic_salary = basic_salary
        self.pf = self.basic_salary*0.12
        self.pt = 200
        self.hra = self.basic_salary*0.5
        self.medical_allowance = medical_allowance

    def calculate_salary(self):
        gross = self.pf + self.pt + self.hra + self.basic_salary
        net = gross - self.pf - self.pt

        return gross,net

    def show_details(self):
        print("ID: {}, Name: {}, Basic salary: {}, PF: {}, PT:{}, HRA: {}, Medical allowance: {}".format(self.empid,self.ename,self.basic_salary,self.pf, self.pt,self.hra,self.medical_allowance))

emp1 = Employee(1,"AAA",10000,2000)
emp1.calculate_salary()
emp1.show_details()


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

man1 = Manager(2, "BBB", 20000, 1000)
man1.calculate_salary()
man1.show_details()

class MarketingExecutive(Employee):
    def __init__(self, empid, ename, basic_salary, medical_allowance, kms_travelled):
        super().__init__(empid, ename, basic_salary, medical_allowance)
        self.kms_travelled = kms_travelled
        self.phone_allowance = 1000
        self.travel_allowance = 5 *self.kms_travelled

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


marexe1 = MarketingExecutive(3, "CCC", 30000, 7500, 56)
marexe1.calculate_salary()
marexe1.show_details()





