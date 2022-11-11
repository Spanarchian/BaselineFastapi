from urllib import response
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List

from fastapi.middleware.cors import CORSMiddleware

from .endpoints.event import router as eventrouter
from .endpoints.blog import router as blogrouter
from .endpoints.video import router as videorouter
from .endpoints.user import router as authrouter
from .endpoints.auth import router as userrouter
from .endpoints.philo import router as philorouter

import neo4j

Philo_list = []

class Philosophers(BaseModel):
    """Represents a philosopher."""
    name: str
    time: str
    nationality: str
 
app = FastAPI()
origins = [
    "http://baselinefastapi.herokuapp.com/",
    "https://baselinefastapi.herokuapp.com/",
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:8100",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(eventrouter)
app.include_router(blogrouter)
app.include_router(videorouter)
app.include_router(userrouter)
app.include_router(authrouter)
app.include_router(philorouter)

Philo_list = [{"name":"Su, Lao", "nationality":"Chinese", "time":"6th BC"},{"name":"Epititus","nationality": "Greek","time": "3rd BC"},{"name":"Watts, Alan", "nationality":"English","time": '20th'}]
   

@app.get("/")
async def root():
    return {"code":418, "message": "I am not the teapot your looking for!"}


@app.get("/stoics")
async def stoics():
    return {
        """{
            "qt_1": {"qt": "Waste no more time arguing what a good man should be. Be One.", "qtr":"Marcus Aurelius"},
            "qt_2": {"qt": "You could leave life right now. Let that determine what you do and say and think.", "qtr":"Marcus Aurelius"},
            "qt_3": {"qt": "He who fears death will never do anything worth of a man who is alive.", "qtr":"Seneca"},
            "qt_4": {"qt": "Life is very short and anxious for those who forget the past, neglect the present, and fear the future.", "qtr":"Seneca"},
            "qt_5": {"qt": "How long are you going to wait before you demand the best for yourself?.", "qtr":"Epictetus"},
            "qt_6": {"qt": "Don’t explain your philosophy. Embody it.", "qtr":"Epictetus"},
            "qt_7": {"qt": "You have power over your mind .", "qtr":" not outside events. Realize this, and you will find strength.―Marcus Aurelius"},
            "qt_8": {"qt": "Hang on to your youthful enthusiasms .", "qtr":" you’ll be able to use them better when you’re older.―Seneca"},
            "qt_9": {"qt": "Wealth consists not in having great possessions, but in having few wants.―Epictetus"},
            "qt_10": {"qt": "If it is not right, do not do it; if it is not true, do not say it.", "qtr":" Marcus Aurelius"},
            "qt_11": {"qt": "Begin at once to live, and count each separate day as a separate life.", "qtr":"Seneca"},
            "qt_12": {"qt": "Stop drifting…Sprint to the finish. Write off your hopes, and if your well-being matters to you, be your own savior while you can.", "qtr":"Marcus Aurelius"},
            "qt_13": {"qt": "Whatever can happen at any time can happen today.", "qtr":"Seneca"},
            "qt_14": {"qt": "They lose the day in expectation of the night, and the night in fear of the dawn.", "qtr":"Seneca"},
            "qt_15": {"qt": "Let us prepare our minds as if we’d come to the very end of life. Let us postpone nothing. Let us balance life’s books each day… The one who puts the finishing touches on their life each day is never short of time.", "qtr":"Marcus Aurelius"},
            "qt_16": {"qt": "True happiness is to enjoy the present, without anxious dependence upon the future, not to amuse ourselves with either hopes or fears but to rest satisfied with what we have, which is sufficient, for he that is so wants nothing. The greatest blessings of mankind are within us and within our reach. A wise man is content with his lot, whatever it may be, without wishing for what he has not.", "qtr":"Seneca"},
            "qt_17": {"qt": "The key is to keep company only with people who uplift you, whose presence calls forth your best.", "qtr":"Epictetus"},
            "qt_18": {"qt": "The happiness of your life depends upon the quality of your thoughts.", "qtr":"Marcus Aurelius"},
            "qt_19": {"qt": "If you want to improve, be content to be thought foolish and stupid.", "qtr":"Epictetus"},
            "qt_20": {"qt": "Luck is what happens when preparation meets opportunity.", "qtr":"Seneca"}
        }"""
    }
    
       
@app.get("/philosophers/", response_model = List[Philosophers])
async def philosophers():
    return Philo_list

@app.post("/philospers/")
async def philospers(philo: Philosophers):
    Philo_list.append(philo)    
    return philo

@app.get('/philosophers/{name}')
async def get_philosopher(name: int):
    try:
        return Philo_list[name]
    except:
        raise HTTPException(status_code=404, detail= f"Philosopher {name} Not Found")
