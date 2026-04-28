# Starter Code for Building REST APIs with FastAPI

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    description: str | None = None

items = [
    Item(id=1, name='Sample Item', description='A starter item for the API')
]

@app.get('/')
def read_root():
    return {'message': 'Welcome to the FastAPI REST API'}

@app.get('/items/{item_id}')
def read_item(item_id: int):
    return {'item_id': item_id}

@app.post('/items/')
def create_item(item: Item):
    items.append(item)
    return item

# TODO: Add more endpoints for update, delete, or list operations
# TODO: Add query parameter support and return full JSON responses
# TODO: Document how to run the app with `uvicorn starter-code:app --reload`
