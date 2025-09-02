from fastapi import FastAPI


"""
# to run use this:
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

# or this command in terminal (this will automatically reload when saving changes):
`uvicorn main:app --reload`

# list of all endpoints:
http://127.0.0.1:8000/docs
"""

app = FastAPI()     # create a FastAPI instance


my_dict = {
    "name": "Alice1",
    "age": 30,
    "city": "New York"
}


# --------------------------------------------------------------------------------
# http://127.0.0.1:8000/example/list
@app.get("/example/list")
async def first_api_endpoint():
    return my_dict


# http://127.0.0.1:8000/example/id/{item_id}
@app.get("/example/id/{item_id}")
async def get_item_by_id(item_id: int):
    return {"item_id": item_id, "name": my_dict.get("name")}





