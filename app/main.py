from fastapi import FastAPI

from .mons.router import mon_router

app = FastAPI()

app.include_router(mon_router)