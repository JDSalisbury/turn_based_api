from fastapi import APIRouter


base_router = APIRouter()


@base_router.get('/')
async def router_list():

    return 'Ok'
