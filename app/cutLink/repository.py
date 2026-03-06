from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from settings.settings import settings
from .models import Link_ORM
from sqlalchemy import select


engine = create_async_engine(url=settings.URL,)
local_session = async_sessionmaker(engine)

async def get_db()->AsyncSession:
    async with local_session() as session:
        yield session


class Store:
    def __init__(self, session: AsyncSession):
        self.session = session
    
    async def input_data(self, data: dict):
        new_data = Link_ORM(
            source = data['source'],
            short = data['short'],
            count = 0
        )
        self.session.add(new_data)
        await self.session.commit()
        return 'Data saved!'
    
    async def read_data(self)->list[Link_ORM]:
        result = await self.session.execute(select(Link_ORM))
        return result.scalars().all()
    
    async def read_data_by_short_id(self, short_id):
        query = select(Link_ORM).where(Link_ORM.short == short_id)
        result = await self.session.execute(query)
        return result.scalars().first()
    
    async def read_data_by_source_link(self, source_link: str):
        query = select(Link_ORM).where(Link_ORM.source == source_link)
        result = await self.session.execute(query)
        return result.scalars().first()
