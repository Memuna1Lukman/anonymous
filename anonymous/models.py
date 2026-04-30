from .database import Base
from sqlalchemy import Column,String,Boolean,text,TIMESTAMP,Integer,ForeignKey,Numeric
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "user"

    id = Column(Integer,primary_key=True)
    email = Column(String,index=True,nullable=False)
    username = Column(String,index=True,nullable=False,unique=True)
    password = Column(String,nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    
class Senders(Base):
    __tablename__ = "senders"
    id = Column(Integer,primary_key=True)
    content = Column(String,index=True,nullable=False)
    user_id = Column(Integer,ForeignKey("user.id",ondelete='CASCADE'),nullable=False)
    ids =   relationship("User")
    sent_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    ip_address = Column(String)