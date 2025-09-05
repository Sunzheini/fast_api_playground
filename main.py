from fastapi import FastAPI

from routers import auth, users


app = FastAPI(title="My AI App")                # create a FastAPI instance
app.include_router(auth.router)                 # include the authentication router
app.include_router(users.router)                # include the users router


# ToDo: fix error not showing
@app.get("/healthy")
async def health_check():
    return {"status": "ok"}
