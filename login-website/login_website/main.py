from fastapi import Depends, FastAPI, HTTPException, status
from login_website import models, schemas, database, crud
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
app = FastAPI()


async def get_session():
    session: AsyncSession = database.SessionLocal()
    try:
        yield session
    finally:
        await session.close()


@app.on_event("startup")
async def startup():
    async with database.engine.connect() as conn:
        await conn.run_sync(schemas.Base.metadata.create_all)


@app.on_event("shutdown")
async def shutdown():
    await database.engine.dispose()


@app.post("/register", status_code=status.HTTP_201_CREATED, response_model=models.User)
async def register(user: models.UserCreate, session: AsyncSession = Depends(get_session)) -> models.User:
    try:
        user = await crud.create_user(session, user)
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Email already exists")
    return user
