from typing import Optional
from pydantic import BaseModel



class TodoCreate(BaseModel):
    text: str
    status: bool


class TodoRead(BaseModel):
    id: int
    text: str
    status: bool
    
    
    class Config:
        orm_mode = True

class TodoUpdate(BaseModel):
    text: Optional[str]
    status: Optional[bool]