from sqlalchemy import Column,Integer,String
from db import Base

#---model---
class unvsv(Base):
    #---table name---
    __tablename__ = 'users'
    #--column---
    #userID
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    #userName
    user_name = Column(String(200),nullable=True)
    #password
    password = Column(String(200),nullable=True)

