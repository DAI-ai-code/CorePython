class Employee:
    eid = 1
    ename = "Abc"
    esala = 99000

    def empDetails(self):
        print("ID: {}".format(self.eid))
        print("NAME: {}".format(self.ename))
        print("SALARY: {}".format(self.esala))


e1 = Employee()
e1.empDetails()


