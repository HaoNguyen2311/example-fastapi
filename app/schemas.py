from typing import Optional
from pydantic import BaseModel, EmailStr, conint
from datetime import datetime


# pydantic modal is use for define structure you want receive from FE

class UserResponse(BaseModel):
  id: int
  email: EmailStr
  create_at: datetime
  # you can see owner: UserResponse in PostBase we must have orm_mode = True
  class Config:
        orm_mode = True

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True
    owner: UserResponse

class PostCreate(PostBase):
  pass

# when u have PostBase u will inherit title content published
class PostResponse(PostBase):
    owner: UserResponse
    id: int
    create_at: datetime
    user_id: int
    
    class Config:
        orm_mode = True
        
        
class PostOut(BaseModel):
    Post: PostResponse
    number_votes:int
    
    class Config:
        orm_mode = True

class UserEmailPassword(BaseModel):
    email: EmailStr
    password: str
    

        
class UserLogin(BaseModel):
  email: EmailStr
  password: str
  
class Token(BaseModel):
  access_token: str
  token_type: str
  
class TokenData(BaseModel):
  id: Optional[str] = None
  

class Vote(BaseModel):
  post_id: int
  # 0 false 1 true
  direction: conint(le=1)    



