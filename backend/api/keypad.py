from fastapi import APIRouter
import uuid

# models.keypad가 아니라 models_keypad라면 import 경로 주의 (보통 폴더 구조상 models.keypad가 맞음)
from models.keypad import KeypadResponse
from services.keypad_service import generate_keypad
from store.session_store import save_session

router = APIRouter()

# 1. 경로에 따옴표 추가 ("/init")
@router.post("/init", response_model=KeypadResponse)
def init_keypad():  # 2. 콜론 추가
    session_id = uuid.uuid4().hex
    
    # 3. 키패드 생성 (여기서 각 키는 dict 형태임: {'type':..., 'id':..., 'value':...})
    layout = generate_keypad()

    # 4. 세션 저장용 맵 생성 (ID -> 실제 값)
    # 나중에 사용자가 ID를 보내면 이 맵을 보고 어떤 숫자인지 알기 위함
    token_map = {
        key["id"]: key["value"]    # 구문 수정: key['id']
        for key in layout
        if key["type"] == "number" # 구문 수정: "number"
    }

    save_session(session_id, token_map, ttl=60)

    # 5. 응답 반환 (구문 수정: 콜론 추가)
    return {
        "session_id": session_id,
        "layout": layout,
        "expires_in": 60
    }