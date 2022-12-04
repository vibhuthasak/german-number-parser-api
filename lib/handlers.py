from lib import db, utility


def getAllTask(taskId):
    taskList = None
    if taskId == None:
        taskList = db.getAllTasks()
    else:
        taskList = db.getTask(taskId)
    if taskList["error"]:
        raise Exception(taskList["description"])
    else:
        return taskList["description"]["taskId"]


def deleteTask(taskId):
    task = db.deleteTask(taskId)
    if task["error"]:
        raise Exception(task["description"])
    else:
        return task["description"]["taskId"]
