from typing import List, Dict
from datetime import datetime
from pydantic import BaseModel

class SizeBase(BaseModel):
    SIZE_NAME: str 
    class Config:
        orm_mode = True
    
class Homepage(BaseModel):
    TITLE : str
    PICTURE_PATH : str
    class Config:
        orm_mode = True

class Community(BaseModel):
    CLUB_NAME : str
    PICTUTE_PATH : str
    class Config:
        orm_mode = True

class Rankuser(BaseModel):
    RANKING : int
    FULL_NAME : str
    AVATAR_PATH : str
    TOTAL_DISTANCE : str
    class Config:
        orm_mode = True

class Rankclub(BaseModel):
    CLUB_RANKING : int
    CLUB_NAME : str
    PICTUTE_PATH : str
    CLUB_TOTAL_DISTANCE : str
    class Config:
        orm_mode = True

class Slogan(BaseModel):
    HTML_CONTENT: str 
    class Config:
        orm_mode = True 

class Statistic(BaseModel):
    member : int
    total_distance : float
    total_club : int
    total_race : int
    class Config:
        orm_mode = True 

class Home(BaseModel):
    homepage : List[Homepage]
    community : List[Community]
    rankuser : List[Rankuser]
    rankclub : List[Rankclub]
    slogan : List[Slogan]
    statistic: Statistic
    class Config:
        orm_mode = True
