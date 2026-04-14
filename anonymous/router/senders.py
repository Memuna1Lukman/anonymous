from fastapi import APIRouter,HTTPException,status,Depends
from sqlalchemy.orm import Session
from .. import schemas,models,oauth
from ..database import get_db

router = APIRouter(
    prefix= "/sendermessge",
    tags='Messages'
)


@router.post("/",status_code=status.HTTP_201_CREATED,response_class=schemas.MessageResponse)
def confession_msg(message:schemas.Message,db:Session = Depends(get_db),get_current_user: int = oauth.get_current_user):
    receiver_id = get_current_user.id
    sent_message = message.dict()
    sent_message["user_id"] = receiver_id
    sent_message = models.Senders(**sent_message)
    
    db.add(sent_message)
    db.commit()
    db.refresh(sent_message)
    return {"MSG": "Successful"}



@router.get("/",response_model=schemas.GetMessage)
def get_confession(db:Session = Depends(get_db),get_current_user: int = oauth.get_current_user):
    query_user = db.query(models.User).filter(models.User.id == get_current_user.id).first()
    if not query_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Userr not found")
    query_message = db.query(models.Senders).filter(models.Senders.user_id == get_current_user.id).all()
    if not query_message:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="You have no messages")
    return query_message

