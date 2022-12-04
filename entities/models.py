from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Task(Base):
    __tablename__ = "tasks_1"

    task_id = Column(Integer, primary_key=True, autoincrement="auto")
    entry_time = Column(DateTime, nullable=False)
    completed_time = Column(DateTime)
    status = Column(String(10), nullable=False)

    def __repr__(self) -> str:
        return super().__repr__()

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Result(Base):
    __tablename__ = "tasks_result"

    result_id = Column(Integer, primary_key=True, autoincrement="auto")
    entry_time = Column(DateTime)
    number = Column(Integer)
    task_id = Column(Integer, ForeignKey("tasks_1.task_id"), nullable=False)

    # task = relationship("Task", back_populates="tasks_results")

    def __repr__(self) -> str:
        return super().__repr__()

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
