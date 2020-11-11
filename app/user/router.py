from fastapi import APIRouter, Depends
from .classes import oauth2_scheme, User, get_current_user, OAuth2PasswordRequestForm, fake_users_db, HTTPException, UserInDB, fake_hash_password

user_router = APIRouter()


@user_router.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    print(form_data.username)
    user_dict = fake_users_db.get(form_data.username)
    print(user_dict)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = UserInDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": user.username, "token_type": "bearer"}


@user_router.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user