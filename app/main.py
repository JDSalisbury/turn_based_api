from fastapi import FastAPI

from .mons.router import mon_router
from .user.router import user_router
from .base.router import base_router
app = FastAPI()

app.include_router(mon_router)
app.include_router(user_router)
app.include_router(base_router)
