import datetime
from pymongo import MongoClient
from bson.json_util import dumps
from bson.objectid import ObjectId
import logging

logger = logging.getLogger(__name__)

client = MongoClient(
    "mongodb://master1:EnybGU522#xLZw@docdb-2022-12-05-07-41-33.cluster-cnpeiwumekol.ap-southeast-1.docdb.amazonaws.com:27017/?replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false",
    connect=False,
)


def createInitalTask():
    try:
        document = {
            "entry_time": datetime.datetime.utcnow(),
            "status": "initial",
            "completed_time": None,
            "results": None,
        }
        response = client.externaldb.tasks.insert_one(document)
        print(response)
        return {"error": False, "description": {"taskId": str(response.inserted_id)}}
    except Exception as error:
        logger.exception("Save failed")
        return {"error": True, "description": str(error)}


def getAllTasks():
    try:
        response = client.externaldb.tasks.find({}).distinct("_id")
        return {"error": False, "description": {"taskId": [str(id) for id in response]}}
    except Exception as error:
        logger.exception("Select failed")
        return {"error": True, "description": str(error)}


def getTask(taskId):
    try:
        response = client.externaldb.tasks.find_one(
            {"_id": ObjectId(taskId)}, {"results": 0}
        )
        if response != None:
            return_dict = {
                "task_id": str(response["_id"]),
                "entry_time": response["entry_time"],
                "status": response["status"],
                "completed_time": response["completed_time"],
            }
            return {"error": False, "description": {"taskId": return_dict}}
        else:
            return {"error": False, "description": {"taskId": None}}
    except Exception as error:
        logger.exception("Select failed")
        return {"error": True, "description": str(error)}


def deleteTask(taskId):
    try:
        response = client.externaldb.tasks.delete_one({"_id": ObjectId(taskId)})
        Isdeleted = False
        if (response.deleted_count == 1):
            Isdeleted = True
        return {"error": False, "description": {"taskId": Isdeleted}}
    except Exception as error:
        logger.exception("Select failed")
        return {"error": True, "description": str(error)}
