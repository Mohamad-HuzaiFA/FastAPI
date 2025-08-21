from pydantic import BaseModel, confloat



class Item_in(BaseModel):
    title : str
    description : str = "No description Added yet"
    price : confloat(ge = 0.0)


class Item_out(BaseModel):
    id : int
    title : str
    description : str = "No description Added yet"
    price : confloat(ge = 0.0)


