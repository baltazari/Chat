from Data.Db_Conection import engine
from fastapi import FastAPI
from Models import User
from Routers import R_User


app = FastAPI()

app.include_router(R_User.router)
