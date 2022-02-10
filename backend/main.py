from email.policy import default
from fastapi import FastAPI
from django.apps import AppConfig
#from backend.models import MetaUser, User_Type

app = FastAPI()

@app.get('/api/hello')
async def root():
 #   x = MetaUser.objects.get(meta_username='raven88')
    return{"message" : "Hello Ra"}



#class APIConfig(AppConfig):
 #   name='app'
  #  default=False