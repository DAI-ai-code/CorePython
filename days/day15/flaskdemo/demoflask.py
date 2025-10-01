from flask import Flask, request

from days.day11.employee_db_prac.emp_db_class import Employee
from days.day15.flaskdemo.emp_operations import inserter

app = Flask(__name__)

@app.route('/')
def hello_world():
    return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Basic Form</title>
</head>
<body>

    <form action="/submit-data" method="POST">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username">
        <br><br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email">
        <br><br>
        <button type="submit">Submit</button>
    </form>

</body>
</html>"""

def objectifier(data):
    empid = data['empid']
    ename = data['ename']
    esalary = data['esalary']
    return Employee(empid, ename, esalary)

@app.route('/submit-data')
def submitted():
    return "SUP"

@app.route('/hello', methods=['POST'])
def hello():
    print(request.get_json())
    return request.get_json()

@app.route('/insert', methods=['POST'])
def add():
    inserter(objectifier(request.get_json()))
    return "Success"

