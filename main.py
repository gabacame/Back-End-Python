from fastapi import FastAPI
from routers import items, suppliers

app = FastAPI() #Initial context

#Routers
app.include_router(items.app)
app.include_router(suppliers.app)

@app.get("/")
async def root():
    return "Esta es una API para gestionar inventarios"

@app.get("/url")
async def url():
    return {"url_repo":"https://github.com/gabacame/Back-End-Python-API"}

