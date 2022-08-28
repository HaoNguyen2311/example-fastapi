from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .routers import post, user,auth, vote
# . is models.py file
from . import models
from .database import engine, get_db
from .config import settings

# this code will create table and connect db when first start it up
# but when you have alembic you dont need it anymore 
# models.Base.metadata.create_all(bind=engine)


app = FastAPI()

origins = ['*']

# allow_origins is which web site you allow it to use your api. like localhost:3000,.
# if you add ['*'] that mean every domain can access it.  
app.add_middleware(
    CORSMiddleware,
    allow_origins=[],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# while True:
#     try:
#         conn = psycopg2.connect(host='localhost', database='fastapi',
#                                 user='postgres', password='231199', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("database connection successful")
#         break
#     except Exception as error:
#         print("connecting to database fail")
#         print("ERROR:", error)
#         time.sleep(2)
app.get('/')


def root():
  return {'message': 'done'}
        
        
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)