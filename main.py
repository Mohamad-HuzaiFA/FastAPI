from typing import Annotated

from fastapi import Depends, FastAPI, File, UploadFile
from fastapi.security import OAuth2PasswordBearer
from .item import Item

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.get("/items/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}

@app.post("/upload/")
async def upload(file: UploadFile = File(...)):
    return {"filename": file.filename}

@app.post("/create_item/")
async def create_item(item : Item):
    return item