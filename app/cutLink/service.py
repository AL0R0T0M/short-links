from .repository import Store, settings
import hashlib
from time import time


class Service:
    def __init__(self, db: Store):
        self.store = db
    
    async def add_data(self, link: str):
        existing_link = await self.store.read_data_by_source_link(link)
        if existing_link:
            return existing_link.short

        hashed = hashlib.md5(link.encode('UTF-8')).hexdigest()
        short = f'http://{settings.DB_HOST}/' + hashed[0:20:2] + f'{int(time())//3600}'
        new_data = {
            'source': link,
            'short': short
        }
        await self.store.input_data(new_data)
        return short
    
    async def get_link(self, short: str):
        data = await self.store.read_data_by_short_id(short)
        source_link = data.source
        return source_link
    
    async def get_data(self):
        return await self.store.read_data()