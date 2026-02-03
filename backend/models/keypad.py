from pydantic import BaseModel
from typing import List, Optional

class Key(BaseModel):
    type: str              # "number" | "empty"
    image: str             # Base64 string
    id: str                # token -> id 로 변경 (프론트엔드와 통일)
    value: str             # 값을 프론트엔드로 전달하기 위해 추가

class KeypadResponse(BaseModel):
    session_id: str
    layout: List[Key]
    expires_in: int