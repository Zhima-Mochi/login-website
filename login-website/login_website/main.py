from fastapi import FastAPI
from login_website import schemas, database
from fastapi.middleware.cors import CORSMiddleware
from login_website.routers.auth import router as auth_router


app = FastAPI()

origins = {
    "*"
}

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(auth_router, prefix="/auth", tags=["Authentication"])


@app.on_event("startup")
async def startup():
    # schemas.Base.metadata.drop_all(bind=database.sync_engine)
    schemas.Base.metadata.create_all(bind=database.sync_engine)
    await database.database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.database.disconnect()
