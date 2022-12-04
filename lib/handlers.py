from lib import db, utility
from werkzeug.utils import secure_filename
import uuid

OBJ_URL = "https://numberfiles-german-numbers.s3.ap-southeast-1.amazonaws.com/"


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


def processFile(file):
    try:
        # Generate Filename, this will use as the key
        fileKey = str(uuid.uuid1().hex)

        # Save on system location
        savedName = f"C:\\Users\Vibhutha\\Desktop\\NavVis-Code-Challenge-Cloud\\german-number-parser\\data\{secure_filename(fileKey)}.txt"
        file.save(savedName)

        # Save task on DB
        dbResponse = db.createInitalTask()
        if not dbResponse["error"]:
            generatedTaskId = dbResponse["description"]["taskId"]
            # Save on S3
            s3Response = utility.saveFileOnS3(savedName, fileKey)
            if not s3Response["error"]:
                s3FileLocationName = OBJ_URL + fileKey + ".txt"
                # Send event to SQS
                event = {"taskId": generatedTaskId, "processFile": s3FileLocationName}

                sqsResponse = utility.publishToProcessQueue(event)
                if not sqsResponse["error"]:
                    return {"error": False, "description": {"taskId": generatedTaskId}}
                else:
                    raise Exception(s3Response["description"])
            else:
                raise Exception(s3Response["description"])
        else:
            raise Exception(s3Response["description"])
    except Exception as e:
        return {"error": True, "description": str(e)}
