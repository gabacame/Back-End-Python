from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

app = APIRouter() #Initial context

# Entidad item
class  Sup(BaseModel):
    id: str
    name: str
    product: str
    price:float

supps_list =[Sup(id='1001', name ="Item 1 sups", product="item 1", price="4"),
             Sup(id='1002', name ="Item 2 sups", product="item 2", price="3"),
             Sup(id='1003', name ="Item 3 sups", product="item 3", price="1"),
             Sup(id='1004', name ="Item 4 sups", product="item 4", price="5")]

@app.get("/supps/")
async def supps():
    return supps_list

@app.get('/supp/{id}')
async def supp(id:str):
    return search_id(id)
        
def search_id(id: str): #Search an item by id
    supp = filter(lambda supp: supp.id == id, supps_list)
    try:
        return list(supp)[0]
    except:
        raise HTTPException(status_code=404, detail="Supp id not found")
            