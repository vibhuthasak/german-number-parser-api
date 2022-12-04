from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import datetime
from entities.models import Task, Result

import logging

logger = logging.getLogger(__name__)

engine = create_engine(
    "mysql+pymysql://extuser:password@docker-for-desktop/external_db",
    echo=True,
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
