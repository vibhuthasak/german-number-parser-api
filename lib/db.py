import datetime
from pymongo import MongoClient
import logging
import sys

logger = logging.getLogger(__name__)

client = MongoClient(
    "mongodb://master1:EnybGU522#xLZw@localhost:27017/?replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false",
    connect=False,
)


def createInitalTask():
    try:
        client.externaldb.tasks.insert_one({"hello": "Amazon DocumentDB"})
        return {"error": False, "description": {"taskId": 1}}
    except Exception as error:
        logger.exception("Save failed")
        return {"error": True, "description": str(error)}


# def getAllTasks():
#     try:
#         return {"error": False, "description": {"taskId": return_list}}
#     except Exception as error:
#         logger.exception("Select failed")
#         return {"error": True, "description": str(error)}


# def getTask(taskId):
#     try:
#         return {"error": False, "description": {"taskId": task.as_dict()}}
#     except Exception as error:
#         logger.exception("Select failed")
#         return {"error": True, "description": str(error)}


# def deleteTask(taskId):
#     try:
#         return {"error": False, "description": {"taskId": task.task_id}}
#     except Exception as error:
#         logger.exception("Select failed")
#         return {"error": True, "description": str(error)}
