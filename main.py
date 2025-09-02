from fastapi import FastAPI

from models.temp_db import DataBaseManager
from views.views import ViewsManager

app = FastAPI()                     # create a FastAPI instance
db_manager = DataBaseManager()      # the "database"
views_manager = ViewsManager(app, db_manager)   # the views


