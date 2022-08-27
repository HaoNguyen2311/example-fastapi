from fastapi import APIRouter, Depends, status, HTTPException,Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ..schemas import UserLogin, Token
from .. import models, utils, oauth2

from ..database import get_db

router = APIRouter(tags=['Authentication'])

@router.post('/login',response_model=Token)
def login(user_credential: OAuth2PasswordRequestForm = Depends() ,db: Session = Depends(get_db)):
  
  # OAuth2PasswordRequestForm = {"username": "example", "password": "example"}
  user = db.query(models.User).filter(models.User.email == user_credential.username).first()
  
  if user == None:
    raise HTTPException(status_code = status.HTTP_403_FORBIDDEN, detail=f"User is not exist")
  
  if not utils.verify(user_credential.password, user.password):
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"User is not exist")
  
  # create a token.
  
  token = oauth2.create_access_token(data = {"user_id": user.id})
  
  return {"access_token": token, "token_type": 'bearer'}