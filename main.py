from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import HTTPException

class Items(BaseModel):
    name:str
    price:float
    in_stock:bool

items_storage={}
id_counter=1

app=FastAPI()

@app.get("/")
def root():
    return{"Message":"api is running"}

@app.post("/items")
def create_item(item:Items):
    global id_counter
    global items_storage
    name=item.name
    price=item.price
    in_stock=item.in_stock
    item_store={
        "ID":id_counter,
        "Name":name,
        "Price":price,
        "In Stock":in_stock
    }
    items_storage[id_counter]=item_store
    id_counter+=1
    return item_store

@app.get("/items")
def show_item(in_stock:bool=None,max_price:float=None):
    global items_storage
    filtered_item_storage={}
    for i in items_storage:
        item=items_storage[i]
        if in_stock is not None and item["In Stock"]!=in_stock:
            continue
        if max_price is not None and item["Price"]>max_price:
            continue
        filtered_item_storage[i]=items_storage[i]
    return filtered_item_storage

@app.get("/items/{item_id}")
def get_item(item_id:int):
    global items_storage
    if item_id not in items_storage:
        raise HTTPException(status_code=404, detail="Item not found")
    return{"Item":items_storage[item_id]}