from pydantic import BaseModel, HttpUrl

class Video(BaseModel, HttpUrl):
    ref: str
    title: str
    desc: str
    creator: str
    modility: str
    theme: str
    type: str
    duration: str
    till: str
    level: str
