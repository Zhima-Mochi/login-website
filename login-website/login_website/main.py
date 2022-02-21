from fastapi import Depends,FastAPI,HTTPException
from login_website.database import engine,SessionLocal

app= FastAPI()

@app.on_event("startup")
async def startup():
    async with engine.connect() as conn:
        await conn.run_sync()

@app.on_event("shutdown")
async def shutdown():
    await engine.dispose()