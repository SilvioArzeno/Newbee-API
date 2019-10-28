from CollegeAPI import db
from sqlalchemy import and_
from .models import Task,TaskSchema
from flask import request,jsonify,Blueprint
from datetime import datetime

app = Blueprint('TaskModule',__name__)
Task_Schema = TaskSchema()
Tasks_Schema = TaskSchema(many = True)

@app.route("/tasks", methods = ["POST"])
def add_task():
    StudentID = request.json['StudentID']
    TaskName = request.json['TaskName']
    TaskDescription = request.json['TaskDescription']
    TaskDueDate = datetime.strptime(request.json['TaskDueDate'],"%Y/%m/%d-%I:%M %p")
    TaskDone = request.json['TaskDone']

    new_task = Task(StudentID,TaskName,TaskDescription,TaskDueDate,TaskDone)

    db.session.add(new_task)
    db.session.commit()

    result = Task.query.filter_by(StudentID = StudentID,
    TaskName = TaskName,
    TaskDueDate = TaskDueDate,
    TaskDescription = TaskDescription, 
    TaskDone = TaskDone).first()

    InsertedTask = Task_Schema.dump(result)

    return Task_Schema.jsonify(InsertedTask)


@app.route("/tasks/<StudentID>", methods = ["GET"])
def get_tasks(StudentID):
    all_tasks = Task.query.filter(Task.StudentID == StudentID)
    resultTasks = Tasks_Schema.dump(all_tasks)
    return jsonify(resultTasks)

@app.route("/tasks/<TaskID>", methods = ["PUT"])
def edit_task(TaskID):
    CurrentTask = Task.query.filter(Task.TaskID == TaskID)
    CurrentTask.TaskName = request.json['TaskName']
    CurrentTask.TaskDescription = request.json['TaskDescription']
    CurrentTask.TaskDueDate = datetime.strptime(request.json['TaskDueDate'],"%Y/%m/%d-%I:%M %p")
    CurrentTask.TaskDone = request.json['TaskDone']

    db.session.commit()

    return jsonify(True)

@app.route("/tasks/<TaskID>", methods = ["DELETE"])
def delete_task(TaskID):
    current_task = Task.query,filter(Task.TaskID == TaskID).first()
    db.session.delete(current_task)
    db.session.commit()

    return jsonify(current_task)
