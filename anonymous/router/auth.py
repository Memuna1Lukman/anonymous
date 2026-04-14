from fastapi import Depends,APIRouter,HTTPException,status
from .. import models,schemas,utils,oauth
from ..database import get_db
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/login",
    tags=['Login']
)



@router.post("/")
def login_user(user: OAuth2PasswordRequestForm = Depends(),db:Session=Depends(get_db)):
    # try:
    log_user = db.query(models.User).filter(models.User.email == user.username).first()
    if not log_user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="You are not an authorrised user")
    verify_password = utils.unhash_password(user.password,log_user.password)
    if not verify_password:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="You are not an authorrised user")
    access_token = oauth.create_access_token(data={"user_id":log_user.id})
    # except TypeError as e:
    #     print(e)
    return{"token": access_token,"token_type":"bearer"}

