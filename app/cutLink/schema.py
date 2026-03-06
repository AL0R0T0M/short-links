from pydantic import BaseModel

class Link(BaseModel):
    source: str
    short: str
    count: int