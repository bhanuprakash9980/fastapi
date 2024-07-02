from fastapi import FastAPI
from starlette.responses import FileResponse 
from fastapi.middleware.gzip import GZipMiddleware

app = FastAPI()

# app.add_middleware(GZipMiddleware)

@app.get("/testing")
def hello_world():
    return {"message": "OK"}

@app.get("/")
async def read_index():
    return FileResponse('app/index.html')