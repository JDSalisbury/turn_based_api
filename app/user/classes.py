from typing import Optional

from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None


class User(BaseModel):
    username: str
    hashed_password: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    active: Optional[bool] = None


class UserInDB(User):
    hashed_password: str
