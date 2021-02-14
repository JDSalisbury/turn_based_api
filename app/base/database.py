import motor.motor_asyncio

from .constants import MONGO_DETAILS

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.galactagagomon

user_collection = database.get_collection("users")


def user_helper(user) -> dict:
    return {
        # "id": str(user["_id"]),
        "username": user['username'],
        "full_name": user['full_name'],
        "email": user['email'],
        # "hashed_password": user['hashed_password'],
        # "active": user['active'],
    }
