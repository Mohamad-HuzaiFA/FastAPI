from pydantic import BaseModel, confloat



class Item(BaseModel):
    id : int
    title : str
    description : str = "No description Added yet"
    price : confloat(ge = 0.0)
    
