from fastapi import APIRouter, Depends
from .service import Service
from .repository import Store, get_db, AsyncSession


router_shortcut_link = APIRouter(
    tags=['LinkTools']
)

def get_service(session: AsyncSession = Depends(get_db)):
    repository = Store(session)
    return Service(repository)

@router_shortcut_link.get('/')
async def get_all_info(service: Service = Depends(get_service)):
    return await service.get_data()

@router_shortcut_link.post('/shorten')
async def shortcut(link: str, service: Service = Depends(get_service)):
    result = await service.add_data(link)
    return result

@router_shortcut_link.get('/stats/{short_id}')
async def get_my_source(short: str, service: Service = Depends(get_service)):
    return await service.get_link(short)