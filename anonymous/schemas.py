from pydantic import BaseModel,EmailStr
from typing import Optional
from datetime import date,datetime

class TokenData(BaseModel):
    id : Optional[int]

#IPvAnyAddress
    


class User(BaseModel):
    id: Optional[int] = None
    email: EmailStr
    password: str
    username: str
    created_at: Optional[datetime] = None
class Users(BaseModel):
    id: Optional[int] = None
    username: str
    created_at : datetime  
    model_config = {"from_attributes": True}
class Message(BaseModel):
    id: Optional[int] = None
    user_id : Optional[int] = None
    content : str
    ip_address : Optional[str] = None
    sent_at: Optional[datetime] = None

class MessageResponse(BaseModel):
    status: str = "successful"
    message: str = "Thank you for confessing"
    sent_at: Optional[datetime] = None 
    model_config = {"from_attributes": True}   


class GetMessage(BaseModel):
    id: Optional[int] = None
    
    content : str
    sent_at: Optional[datetime] = None
    model_config = {"from_attributes": True}
