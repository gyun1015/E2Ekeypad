from pydantic import BaseModel
from typing import List, Optional

class Key(BaseModel):
    type: str              # "number" | "empty"
    image: str
    token: Optional[str]

class KeypadResponse(BaseModel):
    session_id: str
    layout: List[Key]
    expires_in: int
