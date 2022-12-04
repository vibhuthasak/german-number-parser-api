from flask import Flask, request
import lib.handlers as handlers

app = Flask(__name__)


@app.route("/task/all", methods=["GET"])
def getAllTaskIds():
    try:
        taskList = handlers.getAllTask(None)
        return {"error": False, "response": taskList}, 200
    except Exception as e:
        return {"error": True, "response": str(e)}, 500


@app.route("/task/<int:task_id>", methods=["GET", "DELETE"])
def getAllTask(task_id):
    try:
        task = None
        if request.method == "GET":
            task = handlers.getAllTask(task_id)
        if request.method == "DELETE":
            task = handlers.deleteTask(task_id)
        return {"error": False, "response": task}, 200
    except Exception as e:
        return {"error": True, "response": str(e)}, 500


if __name__ == "__main__":
    app.run()
