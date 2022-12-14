from typing import Optional, List
from pydantic import BaseModel
from datetime import datetime

# Authorisation response models
class Token(BaseModel):
    access_token: str
    token_type: str
