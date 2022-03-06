from asyncio.log import logger
from datetime import datetime
from fastapi import Depends, FastAPI, HTTPException, status, Response
from . import models, schemas, database, crud, authentication_tool, password_tool
from starlette import status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


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


@app.on_event("startup")
async def startup():
    # schemas.Base.metadata.drop_all(bind=database.sync_engine)
    schemas.Base.metadata.create_all(bind=database.sync_engine)
    await database.database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.database.disconnect()


@app.post("/register", status_code=status.HTTP_201_CREATED, response_model=models.User)
async def register(user_create: models.UserCreate, connection=Depends(database.get_connection)) -> models.User:
    async with connection.transaction():
        try:
            user_db = await crud.create_user(connection, user_create)
        except Exception as e:
            logger.error(e)
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Email already exists")
        return user_db


@app.post("/token")
async def create_token(response: Response, form_data: OAuth2PasswordRequestForm = Depends(OAuth2PasswordRequestForm), connection=Depends(database.get_connection), redis_conn=Depends(database.get_redis_conn)):
    async with connection.transaction():
        email = form_data.username
        password = form_data.password
        user = await authentication_tool.authenticate_user(connection, email, password)
        if user is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
        token, expire_time = password_tool.create_access_token(data={
                                                               "sub": email})
        await redis_conn.set(email, token, (expire_time-datetime.now()).seconds)
        response.set_cookie(key="session", value=token, expires=expire_time.ctime(),
                            httponly=True, samesite="lax")
        return token
