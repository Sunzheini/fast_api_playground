from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from models.models import User
from models.temp_db import DataBaseManager

router = APIRouter()


# http://127.0.0.1:8000/login
# Accept application/x-www-form-urlencoded form data with the fields of the User model
@router.post("/login")
async def get_user(form_user: User = Depends(User.as_form)):
    # In a real application, you would verify the provided user fields here.

    entered_user_name = form_user.name
    bd = DataBaseManager

    for user in bd.users_db:
        if user.name == entered_user_name:
            return {"access_token": user.name, "token_type": "bearer"}

    return None
