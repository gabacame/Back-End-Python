from fastapi import FastAPI

app = FastAPI() #Initial context

@app.get("/")
async def root():
    return "Esta es una API para gestionar inventarios"

@app.get("/url")
async def url():
    return {"url_repo":"https://github.com/gabacame/Back-End-Python-API"}

