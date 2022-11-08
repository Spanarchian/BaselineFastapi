from pydantic import BaseModel, HttpUrl

class Blog(BaseModel, HttpUrl):
    ref: int
    title: str
    desc: str
    creator: str
    modility: str
    status: str

