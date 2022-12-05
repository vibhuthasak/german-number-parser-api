from flask import Flask, request
import lib.handlers as handlers
from lib import utility

app = Flask(__name__)


@app.route("/task/all", methods=["GET"])
def getAllTaskIds():
    try:
        taskList = handlers.getAllTask(None)
        return {"error": False, "response": taskList}, 200
    except Exception as e:
        return {"error": True, "response": str(e)}, 500


@app.route("/task/<string:task_id>", methods=["GET", "DELETE"])
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


@app.route("/process", methods=["POST"])
def processFile():
    try:
        file = request.files
        if "file" not in file:
            return {"error": True, "response": "No file on the request"}, 400
        # Validate file
        reqFile = file["file"]
        if not utility.fileValidator(reqFile):
            return {"error": True, "description": "File Validation failed"}, 400
        fileResponse = handlers.processFile(reqFile)
        if not fileResponse["error"]:
            return {"error": False, "response": fileResponse["description"]}, 200
        else:
            raise Exception(fileResponse["description"])
    except Exception as e:
        return {"error": True, "response": str(e)}, 500


if __name__ == "__main__":
    app.run()
