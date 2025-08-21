from typing import Annotated

from fastapi import Depends, FastAPI, File, UploadFile
from fastapi.security import OAuth2PasswordBearer
from .item import Item_in,Item_out

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

fake_db = []
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