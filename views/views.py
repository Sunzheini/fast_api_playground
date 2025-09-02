from fastapi import FastAPI, Body, HTTPException

from models.temp_db import DataBaseManager


class ViewsManager:
    def __init__(self, app: FastAPI, db: DataBaseManager):
        self.app = app
        self.db = db
        self.register_views()

    def register_views(self):
        #GET list
        # http://127.0.0.1:8000/list
        @self.app.get("/list")
        async def list_users():
            return self.db.users_db

        # GET one
        # http://127.0.0.1:8000/id/2
        @self.app.get("/id/{user_id}")
        async def get_user(user_id: int):
            for user in self.db.users_db:
                if user["id"] == user_id:
                    return user
            raise HTTPException(status_code=404, detail="User not found with path parameter")

        # POST
        # http://127.0.0.1:8000/create
        # request body (application/json)
        # {"name": "Alice3", "age": 30, "city": "New York", "email": "alice@example.com"}
        # {"name": "Alice4", "age": 30, "city": "New York", "email": "alice@example.com"}
        @self.app.post("/create")
        async def create_user(new_item=Body()):
            next_id = self.db.next_id

            new_user = {
                "id": next_id,
                "name": new_item.get("name"),
                "age": new_item.get("age"),
                "city": new_item.get("city"),
                "email": new_item.get("email")
            }

            self.db.users_db.append(new_user)
            self.db.next_id += 1
            return new_user
