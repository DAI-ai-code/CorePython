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
updater(2,49000)