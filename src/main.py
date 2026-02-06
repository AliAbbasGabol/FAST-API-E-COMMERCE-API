from fastapi import FastAPI, Query, HTTPException, status
from enum import Enum
from pydantic import BaseModel
from typing import Annotated
app = FastAPI()



class product(BaseModel):
    name: str
    price: int
    category: str
    creator: str | None = None

class category_select(str, Enum):
    food = "alexer"
    drinks = "reseter"
    cloths = "hotter"



@app.get("/")
def intro():
    return {"hello"}


@app.get("/product/{id}")
def get_product(id: int):
    return {"id": id}

@app.get("/products/{category}")
def namer(category: category_select):
    if category == category_select.food:
        return {"this is food"}
    elif category == category_select.cloths:
        return {"damn has to cloths"}
    else:
        return {"so u is drinky"}
    

@app.post("/product")
def add_product(item: product):
    items = item.model_dump()
    items.update({"price": 133})
    return items

@app.put("/producs/{id}" )
def update_product(id: int, price: Annotated[int, Query(ge=1, le=999999)], phone: Annotated[int, Query(ge=100000000000, le=9999999999999)], email: Annotated[str, Query(pattern= "^[a-zA-z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$")]):
    return price
     