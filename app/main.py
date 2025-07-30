from fastapi.security import OAuth2PasswordBearer
from fastapi import FastAPI

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

from app import endpoint
