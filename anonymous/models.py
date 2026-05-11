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
    sender = relationship("Senders",back_populates="users")
class Senders(Base):
    __tablename__ = "senders"
    id = Column(Integer,primary_key=True)
    content = Column(String,index=True,nullable=False)
    user = Column(String,ForeignKey("user.username",ondelete='CASCADE'),nullable=False)
    users =   relationship("User",back_populates="sender")
    sent_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    ip_address = Column(String,nullable=False)