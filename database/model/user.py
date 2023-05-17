from peewee import IntegerField, DateField
from database.model.model_base import ModelBase

class User(ModelBase):
    vk_id = IntegerField()
    brain_size = IntegerField()
    brain_size_last_update = DateField()