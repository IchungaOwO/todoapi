from sqlalchemy import Column, Integer, String, ForeignKey
from models.tag import task_tag 
from database import Base
from sqlalchemy.orm import relationship

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    owner_id = Column(Integer, ForeignKey("users.id")) 

    tags = relationship(
    "Tag",
    secondary=task_tag,
    back_populates="tasks"
    )