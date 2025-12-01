import os
from fastapi import FastAPI, UploadFile, File, HTTPException
from app.ai_service import transcribe_audio as transcribe_audio_service
from app.core.config import settings

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the audio transcription service"}

@app.post("/transcribe/")
async def transcribe_audio(file: UploadFile = File(...)):
    try:
        audio_bytes = await file.read()
        transcription = transcribe_audio_service(audio_bytes, file.content_type)
        return {"transcription": transcription}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
