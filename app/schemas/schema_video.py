from pydantic import BaseModel, HttpUrl

class Video(BaseModel, HttpUrl):
    ref: int
    title: str
    desc: str
    creator: str
    modility: str
    theme: str

