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
dammer = []
for i in damm:
    if i!='':
        dammer.append(i.split(','))


l = []
for i in range(3):
    d= {}
    for j in range(3):
        exp = dammer[i][j].strip().split(' : ')
        d[exp[0]] = exp[1]
    else:
        l.append(d)
else:
    print(l)

emp_list = []
for i in l:
    empid = i['EMP_ID']
    name = i['name']
    salary = i['salary']
    emp_list.append(Employee(empid, name, salary))

print(type(emp_list[0]))
print(emp_list)

emp_dict = {}
e_id = 1
for i in l:
    empid = i['EMP_ID']
    name = i['name']
    salary = i['salary']
    emp_dict[e_id] = Employee(empid, name, salary)

print(type(emp_dict[1]))
print(emp_dict)





