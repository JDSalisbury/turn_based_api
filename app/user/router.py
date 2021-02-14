from fastapi import APIRouter, Body, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordRequestForm

from ..base.classes import ResponseModel
from .auth import (ACCESS_TOKEN_EXPIRE_MINUTES, authenticate_user,
                   create_access_token, fake_item_db, fake_users_db,
                   get_current_active_user, get_password_hash, timedelta)
from .classes import Token, User
from .db_user_actions import add_user

user_router = APIRouter()


@user_router.post("/create", response_description="User data added into the database")
async def add_user_data(user: User = Body(...)):
    user = jsonable_encoder(user)
    user['hashed_password'] = get_password_hash(user['hashed_password'])
    new_user = await add_user(user)
    return ResponseModel(new_user, "User added successfully.")


@user_router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(
        fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@user_router.get("/users/me/", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user


@user_router.get("/users/me/items/")
async def read_own_items(current_user: User = Depends(get_current_active_user)):

    return [item for item in fake_item_db if item['owner'] == current_user.username]
