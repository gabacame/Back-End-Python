from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI() #Initial context

# Entidad item
class Item(BaseModel):
    id: str
    name: str
    quantity: int
    price: list

items_list=[Item(id="0001",name="Iteam 1",quantity=10,price=[32,"MXN"]),
            Item(id="0002",name="Iteam 2",quantity=14,price=[25,"MXN"]),
            Item(id="0003",name="Iteam 3",quantity=17,price=[64,"MXN"]),
            Item(id="0004",name="Iteam 4",quantity=11,price=[16,"MXN"])]    

@app.get("/itemsjson")
async def itemsjson():
    return [{"id":"0001", "name":"Iteam 1", "quantity": 10, "price":[32,"MXN"]},
            {"iD":"0002", "name":"Iteam 2", "quantity": 14, "price":[25,"MXN"]},
            {"iD":"0003", "name":"Iteam 3", "quantity": 17, "price":[64,"MXN"]},
            {"iD":"0004", "name":"Iteam 4", "quantity": 11, "price":[16,"MXN"]}]

@app.get("/items")
async def items():
    return items_list

#PATH Fix parameters
@app.get("/item/{id}")
async def item(id: str):
    return search_item(id)

#QUERY may not necessary to make the petition
@app.get("/item/")
async def item(id: str):
    return search_item(id)

@app.post("/item/")
async def item(item: Item):

    if type(search_item(item.id))==Item:
        return {"error":"Item ID already exist"}
    else:
        print("Item succefully added to inventory") 
        items_list.append(item)
        return {"succes":"Item succefully added to inventory"}

@app.put("/item/")
async def item(item: Item):
    found = False
    for index,saved_item in enumerate(items_list):
        if saved_item.id == item.id:
            items_list[index] = item
            found = True
            return {"succes":"Item succefully changed in inventory" }
    if not found:
        return {"error":"Item ID not found"}
    
@app.delete("/item/{id}")
async def item(id:str):
        found = False
        for index,saved_item in enumerate(items_list):
            if saved_item.id == id:
                del items_list[index]
                found = True
                return{"succes":"Item succefully deleted to inventory"} 
        if not found:
            return {"error":"Item not deleted"}

#Functios
def search_item(id: str): #Search an item by id
    items = filter(lambda item: item.id == id, items_list)
    try:
        return list(items)[0]
    except:
        return {"error":"Item ID not found"}
