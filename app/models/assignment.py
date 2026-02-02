from sqlalchemy import CheckConstraint, Column, ForeignKey, Integer,String,DateTime,Text
from app.core.database import Base

class AssignmentTable(Base):
    __tablename__ = "Assignment"

    id = Column(Integer,primary_key=True,index=True)
    title = Column(String(50))
    description = Column(String(200))
    subject_name = Column(String(20))
    semester = Column(Integer,CheckConstraint('semester>=1 and semester<=8'),name='semester')
    file_url =  Column(String(100))
    author_id = Column(Integer,ForeignKey('Profile.id'))
    tags = Column(Text)
    created_at = Column(DateTime)