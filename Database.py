from peewee import *
import datetime


db = SqliteDatabase('users.db')

class BaseModel(Model):
    class Meta:
        database = db

class Users(BaseModel):
    ig = CharField(null=True)
    tg = CharField(null=True)



def create_tables():
    with db:
        db.create_tables([Users])