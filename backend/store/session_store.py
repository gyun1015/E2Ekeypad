import time

SESSION_STORE = {}

def save_session(session_id: str, data: dict, ttl: int = 60):
    SESSION_STORE[session_id] = {
        "data": data,
        "expires_at": time.time() + ttl
    }

def get_session(session_id: str):
    session = SESSION_STORE.get(session_id)
    if not session:
        return None

    if session["expires_at"] < time.time():
        del SESSION_STORE[session_id]
        return None

    return session["data"]
