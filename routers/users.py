from fastapi import APIRouter

from models.temp_db import DataBaseManager
from views.views import ViewsManager


router = APIRouter(
    prefix='/users',
    tags=['users'],
)

db_manager = DataBaseManager()                  # the "database"
views_manager = ViewsManager(router)   # the views
