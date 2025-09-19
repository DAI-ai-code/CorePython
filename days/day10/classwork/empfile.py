class Employee:
    def __init__(self, empid, name, salary):
        self.empid, self.name, self.salary = empid, name, salary

    def __repr__(self):
        return f'EMP_ID : {self.empid}, name : {self.name}, salary : {self.salary}'


e1 = Employee('E1', 'AAA', 1000 )
e2 = Employee('E2', 'BBB', 2000 )
e3 = Employee('E3', 'BBB', 5000 )
damm = ''
try:
    f = open("prog8.txt", 'w')
    f.write('')
    f.close()
    f = open("prog8.txt", 'a')
    f.write(str(e1) + '\n')
    f.write(str(e2) + '\n')
    f.write(str(e3) + '\n')
    f.close()
#
    f = open("prog8.txt", 'r')
    data = f.read()
    damm = data
    print(data)

except:
    print('error')

finally:
    f.close()

damm = damm.split('\n')
print(damm)
for i in damm:
    if i!='':
        print(i.split(','))

