from login_website import crud, database, password_tool, dependents, models, authentication_tool
from asyncio.log import logger
import aiofiles
from fastapi import Depends, APIRouter, File, HTTPException, UploadFile, status, Response
from starlette import status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

router = APIRouter()


@router.get("/info", status_code=status.HTTP_200_OK, response_model=models.UserInfo)
async def user_info(userDB=Depends(dependents.get_user_info)):
    return userDB


@router.put("/info", status_code=status.HTTP_202_ACCEPTED, response_model=models.UserInfo)
async def update_user_info(user_info_update: UploadFile = File(...),  is_login: bool = Depends(dependents.is_login)):
    print(user_info_update.filename)
    return None


@router.get("/profile", status_code=status.HTTP_200_OK)
async def user_profile(user_email: str = Depends(dependents.check_authentication), connection=Depends(database.get_connection)):
    image = await crud.get_user_profile(connection, user_email)
    return Response(content=image, media_type="image/png")


@router.put("/profile", status_code=status.HTTP_202_ACCEPTED)
async def update_user_profile(user_profile: UploadFile = File(...), user_email=Depends(dependents.check_authentication), connection=Depends(database.get_connection)):
    if user_profile.content_type not in ["image/png", "image/jpeg"]:
        raise HTTPException(status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)
    content = await user_profile.read()
    
    async with connection.transaction():
        await crud.update_user_profile(connection, user_email, content)
        return
