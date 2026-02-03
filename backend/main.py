from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles   # ✅ 추가

from api.keypad import router as keypad_router

app = FastAPI()

# ✅ CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ static 파일 서빙 설정 (중요)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def health():
    return {"status": "ok"}

app.include_router(keypad_router, prefix="/keypad")
