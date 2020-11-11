from fastapi import FastAPI

from .mons.router import mon_router
from .user.router import user_router
app = FastAPI()

app.include_router(mon_router)
app.include_router(user_router)