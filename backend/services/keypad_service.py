import uuid
import random

def generate_keypad():
    keys = []

    # 숫자 키 0~9
    for n in range(10):
        keys.append({
            "type": "number",
            "image": f"/static/{n}.png",
            "token": uuid.uuid4().hex
        })

    # empty 키 2개
    keys.append({
        "type": "empty",
        "image": "/static/empty.png",
        "token": None
    })
    keys.append({
        "type": "empty",
        "image": "/static/empty.png",
        "token": None
    })

    random.shuffle(keys)
    return keys
