import os
import mimetypes
from fastapi import FastAPI, UploadFile, File, HTTPException, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.ai_service import transcribe_audio as transcribe_audio_service
from app.core.config import settings

app = FastAPI()
security = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Security(security)):
    if credentials.scheme != "Bearer" or credentials.credentials != settings.API_KEY:
        raise HTTPException(
            status_code=401,
            detail="Invalid or missing API key",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return True

@app.get("/")
def read_root():
    return {"message": "Welcome to the audio transcription service"}

@app.post("/transcribe/")
async def transcribe_audio(file: UploadFile = File(...), authorized: bool = Security(get_current_user)):
    try:
        mime_type, _ = mimetypes.guess_type(file.filename)
        if not mime_type or not mime_type.startswith('audio/'):
            raise HTTPException(status_code=400, detail=f"Unsupported file type: {mime_type}. Please upload a valid audio file.")

        audio_bytes = await file.read()
        transcription = transcribe_audio_service(audio_bytes, mime_type)
        return {"transcription": transcription}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
