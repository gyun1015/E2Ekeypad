import os
import base64
import secrets
import uuid

# ✅ [핵심 수정] 프로젝트의 최상위 루트 경로를 확실하게 찾습니다.
# 이 코드가 있는 파일이 'services' 폴더 안에 있다고 가정할 때의 설정입니다.
# __file__ : 현재 파일의 경로
# os.path.dirname : 폴더 경로 추출
# .parent : 상위 폴더로 이동
from pathlib import Path

# 현재 파일 위치: .../project/services/keypad_service.py (예시)
# 목표 static 위치: .../project/static

BASE_DIR = Path(__file__).resolve().parent.parent 
STATIC_DIR = BASE_DIR / "static"

def get_image_as_base64(filename):
    """이미지 파일을 읽어서 Base64로 변환"""
    # 3. 절대 경로로 파일 위치 지정
    file_path = STATIC_DIR / filename
    
    try:
        with open(file_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
            return f"data:image/png;base64,{encoded_string}"
    except FileNotFoundError:
        # ⚠️ 서버 터미널 로그에서 이 메시지가 뜨는지 확인하세요
        print(f"❌ Error: 파일을 찾을 수 없습니다 -> {file_path}")
        return ""

def generate_keypad():
    keys = []
    
    # 0~9 이미지 처리
    for n in range(10):
        # 파일명만 넘김 (경로 결합은 get_image_as_base64 내부에서 함)
        img_base64 = get_image_as_base64(f"{n}.png")
        
        keys.append({
            "type": "number",
            "image": img_base64, # Base64 문자열
            "value": str(n),
            "id": uuid.uuid4().hex
        })

    # Empty 이미지 처리
    empty_base64 = get_image_as_base64("empty.png")
    for _ in range(2):
        keys.append({
            "type": "empty",
            "image": empty_base64,
            "value": "",
            "id": uuid.uuid4().hex
        })

    secrets.SystemRandom().shuffle(keys)
    return keys