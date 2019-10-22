from CollegeAPI import db
from .models import Task,TaskSchema
from flask import request,jsonify,Blueprint
from datetime import datetime

app = Blueprint('TaskModule',__name__)
Task_Schema = TaskSchema()
Tasks_Schema = TaskSchema(many = True)

@app.route("/tasks", methods = ["POST"])
def add_task():
    StudentID = request.json['StudentID']
    TaskID = request.json['TaskID']
    TaskName = request.json['TaskName']
    TaskDescription = request.json['TaskDescription']
    TaskDueDate = datetime.strptime(request.json['TaskDueDate'],"%Y/%m/%d-%I:%M %p")
    TaskDone = request.json['TaskDone']

    new_task = Task(StudentID,TaskID,TaskName,TaskDescription,TaskDueDate,TaskDone)

    db.session.add(new_task)
    db.session.commit()

    return Task_Schema.jsonify(new_task)


@app.route("/tasks/<StudentID>", methods = ["GET"])
def get_tasks(StudentID):
    all_tasks = Task.query.filter(Task.StudentID == StudentID)
    resultTasks = Tasks_Schema.dump(all_tasks)
    return jsonify(resultTasks)

@app.route("/tasks/<StudentID>/<TaskID>", methods = ["GET"])