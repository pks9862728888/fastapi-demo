from typing import Annotated, Union

from fastapi import Depends, Query
from app.exchanges.item import Item
from app.main import app, oauth2_scheme


@app.get("/")
async def root(
    token: Annotated[str, Depends(oauth2_scheme)] = None,
) -> dict:
    return {"message": "Hello"}


@app.get("/test/{path_param}")
async def printPathParam(
    path_param: str,
    token: Annotated[str, Depends(oauth2_scheme)] = None,
) -> dict:
    response: dict = {"path_param": path_param}
    print(response)
    return response


@app.post("/test/{path_param}")
async def printPathParam(
    path_param: int,
    skip: int,
    optional_query_param: Union[str | None] = None,
    token: Annotated[str, Depends(oauth2_scheme)] = None,
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
async def test_body(
    item: Item,
    token: Annotated[str, Depends(oauth2_scheme)] = None,
) -> Item:
    print(item)
    return item


@app.get("/items/")
async def read_items(
    q: Annotated[list[str], Query()] = [],
    token: Annotated[str, Depends(oauth2_scheme)] = None,
):
    query_items = {"q": q, "token": token}
    return query_items
