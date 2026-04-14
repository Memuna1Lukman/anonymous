from fastapi import APIRouter,Depends,HTTPException,status

from .. import models, schemas,utils
from ..database import get_db

from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/signup",
    tags=['Sign Up']
)



@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.Users)
def createUser(user:schemas.User,db:Session=Depends(get_db)):
    hashed = utils.hash_password(user.password)
    new_user = user.dict()
    new_user['password'] = hashed
    new_user=  models.User(**new_user)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

