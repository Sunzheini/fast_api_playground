from fastapi import FastAPI, Body, HTTPException
from typing import List
from models.models import User
from temp_db import users_db, next_id


class ViewsManager:
    def __init__(self, app: FastAPI):
        self.app = app
        self.register_views()

    def register_views(self):
        #GET list
        # http://127.0.0.1:8000/list
        @self.app.get("/list")
        async def list_users():
            return users_db[-1]

        # GET with path parameter
        # http://127.0.0.1:8000/id/1
        @self.app.get("/id/{user_id}")
        async def get_user(user_id: int):
            for user in users_db:
                if user["id"] == user_id:
                    return user
            raise HTTPException(status_code=404, detail="User not found with path parameter")

        # GET with query parameter
        # http://127.0.0.1:8000/list/?id=1
        @self.app.get("/list/")
        async def get_user_query(user_id: int):
            for user in users_db:
                if user["id"] == user_id:
                    return user
            raise HTTPException(status_code=404, detail="User not found with query parameter")
