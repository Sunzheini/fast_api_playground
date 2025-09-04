from fastapi import FastAPI

from routers import auth, users


app = FastAPI()                                 # create a FastAPI instance
app.include_router(auth.router)                 # include the authentication router
app.include_router(users.router)                # include the users router


@app.get("/healthy")
async def health_check():
    return {"status": "ok"}
