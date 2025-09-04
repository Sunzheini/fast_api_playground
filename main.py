from fastapi import FastAPI
from reactpy import component, html
from reactpy.backend.fastapi import configure

from routers import auth, users


app = FastAPI(title="My AI App")                # create a FastAPI instance
app.include_router(auth.router)                 # include the authentication router
app.include_router(users.router)                # include the users router


# ToDo: fix error not showing
@app.get("/healthy")
async def health_check():
    return {"status": "ok"}


# --------------------------------------------------------------------------------------

@component
def HelloWorld():
    return html.h1("Hello, World!")


@component
def App():
    # return html.div(
    #     html.h1("Welcome to the FastAPI and ReactPy Application"),
    #     html.p("This is a simple example of integrating FastAPI with ReactPy."),
    #     HelloWorld(),
    # )
    return html.h1("It Works!")


# Configure ReactPy with FastAPI (version without url_path support)
# We keep the default mount (usually at "/"). The /react page embeds it via iframe to avoid MIME issues.
configure(app, App)
