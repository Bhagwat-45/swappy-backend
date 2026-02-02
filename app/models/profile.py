from sqlalchemy import Boolean, CheckConstraint,Integer,String,Column,DateTime
from app.core.database import Base

class ProfileTable(Base):
    __tablename__ = "Profile"

    id = Column(Integer,primary_key=True,index=True)
    full_name = Column(String(25))
    email = Column(String(100),unique=True)
    hashed_password = Column(String)
    usn_id = Column(String,unique=True)
    college_name = Column(String)
    semester = Column(Integer,CheckConstraint('semester>=1 AND semester<= 8'),name='semester')
    tech_stack = Column(String)
    bio = Column(String(200))
    is_verified = Column(Boolean)
    created_at = Column(DateTime)


    


