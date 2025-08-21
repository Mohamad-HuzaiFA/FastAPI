from typing import Annotated

from fastapi import Depends, FastAPI, File, HTTPException, UploadFile
from fastapi.security import OAuth2PasswordBearer
from .item import Item_in,Item_out

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

fake_db = [
    Item_out(id=1, title="Laptop", description="Gaming laptop", price=1200.5),
    Item_out(id=2, title="Phone", description="Smartphone", price=800.0),
]
counter = 0

@app.get("/items/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}

@app.post("/upload/")
async def upload(file: UploadFile = File(...)):
    return {"filename": file.filename}

@app.post("/create_item/",response_model=Item_out)
async def create_item(item : Item_in):
    global counter
    counter += 1 

    item_out = Item_out(id=counter, **item.model_dump())
    fake_db.append(item_out)

    return item_out


@app.get("/item/{item_id}",response_model=Item_out)
async def get_item(item_id : int):
    for item in fake_db:
        if item.id == item_id:
            return item

    raise HTTPException(status_code=404, detail="Item not found")
    