from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix = '/supps', 
                   tags = ["supps"],
                   responses={404: {"messege":"Not Found"}}) #Initial context

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

@router.get("/")
async def supps():
    return supps_list

@router.get('/{id}')
async def supp(id:str):
    return search_id(id)

@router.post("/",status_code=201)
async def supp(sup: Sup):
    if type(search_id(sup.id))==Sup:
        raise HTTPException(status_code=404, detail = "Item ID already exist")
        #return {"error":"Item ID already exist"}
    else:
        print("Supplier succefully added to Suppliers list") 
        supps_list.append(sup)
        return {"succes":"Supplier succefully added to Suppliers list"}

def search_id(id: str): #Search an item by id
    supp = filter(lambda supp: supp.id == id, supps_list)
    try:
        return list(supp)[0]
    except:
        return {"error":"Item ID not found"}


            