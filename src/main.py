from fastapi import FastAPI, Query, HTTPException, status, Path, Body, Header, Response
from enum import Enum
from pydantic import BaseModel, Field, HttpUrl, EmailStr
from fastapi.responses import JSONResponse, RedirectResponse
from typing import Annotated
app = FastAPI()


class Image(BaseModel):
    url: HttpUrl
    name: str


class product(BaseModel):
    model_config = {"extra": "forbid"}
    name: str
    price: int = Field(ge=1, le=999999,examples= ["price must be under 100,000"])
    category: str
    creator: str | None = Field(default=None, examples=["your name"])
    image: list[Image] | None = None
   

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
def add_product(item: product,user_agent: Annotated[str | None, Header()] = None):
    items = item.model_dump()
    items.update({"price": 133})
    return items

@app.put("/producs/{id}" )
def update_product(id: Annotated[int, Path(title="The ID of the item to get")], price: Annotated[int, Query(ge=1, le=999999)], phone: Annotated[int, Query(ge=100000000000, le=9999999999999)], email: Annotated[str, Query(pattern= "^[a-zA-z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$")], item: Annotated[
        product,
        Body(
           openapi_examples={
                "normal": {
                    "summary": "A normal example",
                    "description": "A **normal** item works correctly.",
                    "value": {
                        "name": "Foo",
                        "description": "A very nice Item",
                        "price": 35.4,
                        "tax": 3.2,
                    },
                },
                "converted": {
                    "summary": "An example with converted data",
                    "description": "FastAPI can convert price `strings` to actual `numbers` automatically",
                    "value": {
                        "name": "Bar",
                        "price": "35.4",
                    },
                },
                "invalid": {
                    "summary": "Invalid data is rejected with an error",
                    "value": {
                        "name": "Baz",
                        "price": "thirty five point four",
                    },
                },
            },
        ),
    ],):
    return price, id
     


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str | None = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None


@app.post("/user/", response_model=UserOut)
async def create_user(user: UserIn) -> any:
    return user


app.get("/portal")
async def get_portal(teleport: bool = False) -> Response:
    if teleport:
        return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    return JSONResponse(content={"message": "Here's your interdimensional portal."})