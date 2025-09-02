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
