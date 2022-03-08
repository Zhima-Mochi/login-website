
from login_website import crud, database, password_tool, dependents, models, authentication_tool
from asyncio.log import logger
from datetime import datetime
from fastapi import Depends, APIRouter, HTTPException, status, Response
from starlette import status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

router = APIRouter()


@router.post("/register", status_code=status.HTTP_201_CREATED, response_model=models.User)
async def register(user_create: models.UserCreate, connection=Depends(database.get_connection)) -> models.User:
    async with connection.transaction():
        try:
            user_db = await crud.create_user(connection, user_create)
        except Exception as e:
            logger.error(e)
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Email already exists")
        return user_db


@router.post("/token")
async def create_token(response: Response, form_data: OAuth2PasswordRequestForm = Depends(OAuth2PasswordRequestForm), connection=Depends(database.get_connection), redis_conn=Depends(database.get_redis_conn)):
    async with connection.transaction():
        user_email = form_data.username
        user_password = form_data.password
        user = await authentication_tool.authenticate_user(connection, user_email, user_password)
        if user is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
        token, expire_time = password_tool.create_access_token(data={
                                                               "sub": user_email})
        await redis_conn.set(user_email, token, (expire_time-datetime.now()).seconds)
        response.set_cookie(key="session", value=token, expires=expire_time.ctime(),
                            httponly=True, samesite="lax")
        return token


@router.get("/login_status")
async def login_status(is_login: bool = Depends(dependents.is_login)):
    return is_login
