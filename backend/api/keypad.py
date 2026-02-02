from fastapi import APIRouter
import uuid

from backend.models.keypad import KeypadResponse
from backend.services.keypad_service import generate_keypad
from backend.store.session_store import save_session

router = APIRouter()

@router.post("/init", response_model=KeypadResponse)
def init_keypad():
    session_id = uuid.uuid4().hex
    layout = generate_keypad()

    # PoC 단계: token -> image 매핑 (숫자 복원은 아직 안 함)
    token_map = {
        key["token"]: key["image"]
        for key in layout
        if key["type"] == "number"
    }

    save_session(session_id, token_map, ttl=60)

    return {
        "session_id": session_id,
        "layout": layout,
        "expires_in": 60
    }
