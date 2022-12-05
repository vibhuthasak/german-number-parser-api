import datetime

import logging

logger = logging.getLogger(__name__)

"mongodb://master1:EnybGU522#xLZw@docdb-2022-12-05-07-41-33.cluster-cnpeiwumekol.ap-southeast-1.docdb.amazonaws.com:27017/?replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false"


def createInitalTask():
    try:
        return {"error": False, "description": {"taskId": task.task_id}}
    except Exception as error:
        logger.exception("Save failed")
        return {"error": True, "description": str(error)}


def getAllTasks():
    try:
        return {"error": False, "description": {"taskId": return_list}}
    except Exception as error:
        logger.exception("Select failed")
        return {"error": True, "description": str(error)}


def getTask(taskId):
    try:
        return {"error": False, "description": {"taskId": task.as_dict()}}
    except Exception as error:
        logger.exception("Select failed")
        return {"error": True, "description": str(error)}


def deleteTask(taskId):
    try:
        return {"error": False, "description": {"taskId": task.task_id}}
    except Exception as error:
        logger.exception("Select failed")
        return {"error": True, "description": str(error)}
