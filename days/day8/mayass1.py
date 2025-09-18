class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def cal_percentage(self):
        p = 0
        for i in self.marks:
            p += self.marks[i]

        return p/len(self.marks)

    def print_info(self):
        print("Name: {}".format(self.name))
        for i in self.marks:
            print("{} : {}".format(i,self.marks[i]))

    @staticmethod
    def max_min_per_finder(l):
        l1= []
        for i in l:
            l1.append(i.cal_percentage())
        return min(l1), max(l1)

a = Student("aaa", {'eng':90, 'sci':80, 'math':45, 'cs':60})
b = a.cal_percentage()
print(b)

a.print_info()

l = []
l.append(Student("bbb", {'eng':70, 'sci':60, 'math':65, 'cs':30}))
l.append(Student("ccc", {'eng':60, 'sci':70, 'math':65, 'cs':50}))
l.append(Student("ddd", {'eng':80, 'sci':90, 'math':75, 'cs':30}))
l.append(Student("eee", {'eng':90, 'sci':80, 'math':75, 'cs':90}))
print(Student.max_min_per_finder(l))





