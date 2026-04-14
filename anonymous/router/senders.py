from fastapi import APIRouter,HTTPException,status,Depends
from sqlalchemy.orm import Session
from .. import schemas,models,oauth
from ..database import get_db

router = APIRouter(
    prefix= "/sendermessge",
    tags='Messages'
)


@router.post("/",status_code=status.HTTP_201_CREATED,response_class=schemas.MessageResponse)
def confession_msg(message:schemas.Message,db:Session = Depends(get_db)):
    sent_message = message.dict()
    sent_message = models.Senders(**sent_message)
    
    db.add(sent_message)
    db.commit()
    db.refresh(sent_message)

