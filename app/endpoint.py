from typing import Union
from fastapi import FastAPI
from app.exchanges.item import Item
from app.main import app


@app.get("/")
async def root() -> dict:
    return {"message": "Hello"}


@app.get("/test/{path_param}")
async def printPathParam(path_param: str) -> dict:
    response: dict = {"path_param": path_param}
    print(response)
    return response


@app.post("/test/{path_param}")
async def printPathParam(
    path_param: int, skip: int, optional_query_param: Union[str | None] = None
) -> dict:
    response: dict = {
        "path_param": path_param,
        "post": True,
        "skip": skip,
        "optional_query_param": optional_query_param,
    }
    print(response)
    return response


@app.post("/test-body/")
async def test_body(item: Item) -> Item:
    print(item)
    return item
