
from ..base.database import user_collection, user_helper
from .auth import verify_password


async def add_user(user_data: dict) -> dict:
    user = await user_collection.insert_one(user_data)
    new_user = await user_collection.find_one({"_id": user.inserted_id})
    return user_helper(new_user)


async def retrieve_user(username: str, password: str) -> dict:
    user = await user_collection.find_one({"username": username})

    if user and verify_password(
            password, user['hashed_password']):
        return user_helper(user)
    else:
        return False
