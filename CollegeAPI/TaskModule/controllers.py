from CollegeAPI import db
from .models import Task,TaskSchema
from flask import request,jsonify,Blueprint

app = Blueprint('TaskModule',__name__)
Task_Schema = TaskSchema()
Tasks_Schema = TaskSchema(many = True)

@app.route("/tasks", methods = ["POST"])
def add_task():
    TaskID = request.json['TaskID']
    TaskName = request.json['TaskName']
    TaskDescription = request.json['TaskDescription']
    TaskDueDate = request.json['TaskDueDate']
    TaskDone = request.json['TaskDone']

    new_task = Task(TaskID,TaskName,TaskDescription,TaskDueDate,TaskDone)

    db.session.add(new_task)
    db.session.commit()

    return Task_Schema.jsonify(new_task)