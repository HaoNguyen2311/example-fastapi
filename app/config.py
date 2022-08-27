from pydantic import BaseSettings

class Settings(BaseSettings):
  database_hostname: str 
  database_port: str 
  database_password: str 
  database_name : str 
  database_username: str
  secret_key: str
  algorithm: str
  access_token_expire_minutes: int
  
  # name must match env like secret_key match SECRET_KEY
  # must class Config
  class Config:
    # must env_file
    env_file = '.env'
  
settings = Settings()