from pydantic import BaseModel
from typing import Optional

class MenuModel(BaseModel):
    link: str
    name: str
    icon: Optional[str] = None
    parent: Optional[str] = None