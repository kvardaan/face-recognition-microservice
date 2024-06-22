from fastapi import FastAPI
from api.routes import api_router

app = FastAPI()
app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000)