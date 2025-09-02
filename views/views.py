from fastapi import FastAPI, HTTPException, Path, Query
from starlette import status as H

from models.models import User
from models.temp_db import DataBaseManager


class ViewsManager:
    def __init__(self, app: FastAPI, db: DataBaseManager):
        self.app = app
        self.db = db

        self.register_views()

    def register_views(self):
        #GET list
        # http://127.0.0.1:8000/list
        @self.app.get("/list", status_code=H.HTTP_200_OK)   # status code if successful
        async def list_users():
            return self.db.users_db

        # GET one with path parameter
        # http://127.0.0.1:8000/id/2
        @self.app.get("/id/{user_id}", status_code=H.HTTP_200_OK)
        async def get_user(user_id: int = Path(gt=0)):  # validation on path parameter
            for user in self.db.users_db:
                if user.id == user_id:
                    return user
            raise HTTPException(status_code=404, detail="User not found with path parameter")

        # GET one with query parameter
        # http://127.0.0.1:8000/list/city?city=Boston
        @self.app.get("/list/", status_code=H.HTTP_200_OK)
        async def get_users_by_city(city: str = Query(min_length=1, max_length=100)):  # validation on query parameter
            users_in_city = [user for user in self.db.users_db if user.city.lower() == city.lower()]
            if not users_in_city:
                raise HTTPException(status_code=404, detail="No users found in the specified city")
            return users_in_city

        # POST
        # http://127.0.0.1:8000/create
        # request body (application/json)
        # {"name": "Alice3", "age": 30, "city": "New York", "email": "alice@example.com"}
        # {"name": "Alice4", "age": 30, "city": "New York", "email": "alice@example.com"}
        @self.app.post("/create", status_code=H.HTTP_201_CREATED)
        async def create_user(new_item: User):
            latest_id: int = len(self.db.users_db)

            new_user = User(
                id=latest_id + 1,
                name=new_item.name,
                age=new_item.age,
                city=new_item.city,
                email=new_item.email
            )

            self.db.users_db.append(new_user)
            return new_user

        # PUT
        # http://127.0.0.1:8000/edit/1
        # request body (application/json)
        # {"name": "Alice2", "age": 30, "city": "New York", "email": "alice@example.com"}
        @self.app.put("/edit/{user_id}", status_code=H.HTTP_204_NO_CONTENT)
        async def edit_user(user_id: int, updated_item: User):
            for user in self.db.users_db:
                if user.id == user_id:
                    user.name = updated_item.name
                    user.age = updated_item.age
                    user.city = updated_item.city
                    user.email = updated_item.email
                    return user

            raise HTTPException(status_code=404, detail="User not found with path parameter")

        # DELETE
        # http://127.0.0.1:8000/delete/3
        @self.app.delete("/delete/{user_id}", status_code=H.HTTP_204_NO_CONTENT)
        async def delete_user(user_id: int = Path(gt=0)):
            for user in self.db.users_db:
                if user.id == user_id:
                    self.db.users_db.remove(user)
                    return {"detail": "User deleted successfully"}

            raise HTTPException(status_code=404, detail="User not found with path parameter")
