from peewee import *

class Connection:
    def __init__(self):
        self.db = SqliteDatabase('resources/data.db')