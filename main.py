from fastapi import FastAPI

from views.views import ViewsManager

app = FastAPI()                     # create a FastAPI instance
views_manager = ViewsManager(app)   # the views
