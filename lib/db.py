from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
import datetime
from entities.models import Task, Result

import logging

logger = logging.getLogger(__name__)

engine = create_engine(
    "mysql+pymysql://extuser:password@docker-for-desktop/external_db",
    future=True,
)


def createInitalTask():
    try:
        with Session(engine) as session:
            task = Task(entry_time=datetime.datetime.now(), status="initial")
            session.add(task)
            session.commit()
            return {"error": False, "description": {"taskId": task.task_id}}
    except Exception as error:
        logger.exception("Save failed")
        return {"error": True, "description": str(error)}


def getAllTasks():
    try:
        with Session(engine) as session:
            querySelecter = select(Task.task_id)
            tasks = session.scalars(querySelecter)
            return_list = []
            for task in tasks:
                return_list.append(task)
            return {"error": False, "description": {"taskId": return_list}}
    except Exception as error:
        logger.exception("Select failed")
        return {"error": True, "description": str(error)}


def getTask(taskId):
    try:
        with Session(engine) as session:
            querySelecter = select(Task).where(Task.task_id == taskId)
            task = session.scalars(querySelecter).one()
            return {"error": False, "description": {"taskId": task.as_dict()}}
    except Exception as error:
        logger.exception("Select failed")
        return {"error": True, "description": str(error)}


def deleteTask(taskId):
    try:
        with Session(engine) as session:
            task = session.get(Task, taskId)
            session.delete(task)
            session.commit()
            return {"error": False, "description": {"taskId": task.task_id}}
    except Exception as error:
        logger.exception("Select failed")
        return {"error": True, "description": str(error)}
