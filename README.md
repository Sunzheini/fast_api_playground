# fast_api_playground


## Install dependencies (Poetry)
poetry add "fastapi[standard]"
poetry add "uvicorn[standard]"


## Start
```
uvicorn main:app --reload

or 

run with a new configuration in PyCharm (no hot reload but stable and you can stop it)
script: D:/Study/Projects/PycharmProjects/fast_api_playground/.venv/Scripts/uvicorn.exe
parameters: main:app --reload --host 127.0.0.1 --port 8000
working directory: D:/Study/Projects/PycharmProjects/fast_api_playground
add environment variables if needed
```


## If it is not stopping with Ctrl+C
```
taskkill /f /im uvicorn.exe
taskkill /f /im python.exe
```
and delete the __pycache__ folders


## Docs
Open Swagger UI: http://127.0.0.1:8000/docs


## `Depends` keyword
The Depends keyword is one of the most powerful features in FastAPI. It's the dependency injection 
system that makes FastAPI so clean and modular.

```
from fastapi import Depends

def my_dependency():
    return "some value"

@app.get("/items/")
async def read_items(value: str = Depends(my_dependency)):
    return {"value": value}
```
What Happens:
    FastAPI sees Depends(my_dependency)
    It calls my_dependency() function
    It passes the return value to your route function as value
    Your route uses the value