from peewee import Model, PrimaryKeyField
from database.connection import Connection

class ModelBase(Model):
    id = PrimaryKeyField(unique=True)

    class Meta:
        database = Connection().db