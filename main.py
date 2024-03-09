from fastapi import FastAPI

from api_listener.routers import router as api_listener_router

app = FastAPI()

app.include_router(router=api_listener_router, prefix="/api_listener")


@app.get("/")
async def root():
    return {"message": "Hello Guys!"}

