from fastapi import status, HTTPException, Depends, APIRouter, Response
from sqlalchemy.orm import Session
from app import models, utils
from ..schemas import UserEmailPassword, UserResponse
# from .. import utils, models

from ..database import engine, get_db


router = APIRouter(
  prefix='/users',
   tags=["Users"]
)


@router.post('/', status_code=status.HTTP_201_CREATED,response_model=UserResponse)
def create_user(email_password: UserEmailPassword,db: Session = Depends(get_db)):

    # hash email_password.password
    hashed_password = utils.hash(email_password.password)
    email_password.password = hashed_password
  
    new_user = models.User(**email_password.dict())
    print(new_user)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
  
@router.get('/{id}',response_model=UserResponse)
def get_user(id:int,db: Session = Depends(get_db)):
     user =  db.query(models.User).filter(models.User.id == id).first()
     if user == None:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"can not found user with id: {id}")
     return user