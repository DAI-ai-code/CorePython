import pymongo

from days.day11.mongodbEmpQues.emp_mongo_db import Employee

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mongoEmployee"]
emp = db["employee"]

def inserter(empid,ename,salary):
    e1  = Employee(empid,ename,salary)
    # print(e1.__repr__())
    emp.insert_one(e1.__repr__())

def updater(empid,salary):
    emp.update_one({"empid":empid},{'$set': {"salary": salary}})


def deleter(empid):
    emp.delete_one({"empid":empid})

def selector(empid):
    emp.find({"empid":empid})

def selector_all():
    c = emp.find()
    # for i in c:
    #     print(i)
    print(list(c))
selector_all()