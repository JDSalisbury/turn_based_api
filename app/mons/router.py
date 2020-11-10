from fastapi import APIRouter

from .classes import *

mon_router = APIRouter()

@mon_router.get('/mon/{lvlstatus}', tags=['mon'])
async def read_mon(lvlstatus: str):
    mon_class = globals()[lvlstatus]
    return mon_class.random_mon()
