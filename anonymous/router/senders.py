from fastapi import APIRouter,HTTPException,status,Depends,Request
from sqlalchemy.orm import Session
from .. import schemas,models,oauth
from ..database import get_db
from datetime import datetime,timedelta
router = APIRouter(
    prefix= "/sendermsg",
    tags=['Messages']
)


@router.post("/{username_id}",status_code=status.HTTP_201_CREATED,response_model=schemas.MessageResponse)
def confession_msg(request : Request,username_id:int,message:schemas.Message,limit=5,db:Session = Depends(get_db)):
    user= db.query(models.User).filter(models.User.id==username_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    now= datetime.utcnow()
    window_minutes=timedelta(minutes=1)
    client_ip = request.client.host
    query_user=db.query(models.Senders).filter(
        models.Senders.user_id == username_id,
        models.Senders.sent_at >= (now-window_minutes),
        models.Senders.ip_address == client_ip
    ).count()
    if query_user >= limit:
        raise HTTPException(status_code=status.HTTP_429_TOO_MANY_REQUESTS,detail=f"Too many requestions try after a minute") 
    sent_message = message.dict()
    sent_message['user_id'] = username_id
   
    sent_message = models.Senders(
        content=message.content,
        user_id=username_id,
        ip_address=client_ip
    )
    # Add rate limiting
    db.add(sent_message)
    db.commit()
    db.refresh(sent_message)
    return {"status": "successful", "message": "Thank you for confessing"}



@router.get("/",response_model=list[schemas.GetMessage])
def get_confession(db:Session = Depends(get_db),get_current_user: int = Depends(oauth.get_current_user)):
    query_user = db.query(models.User).filter(models.User.id == get_current_user.id).first()
    if not query_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Userr not found")
    query_message = db.query(models.Senders).filter(models.Senders.user_id == get_current_user.id).all()
    
    return query_message

