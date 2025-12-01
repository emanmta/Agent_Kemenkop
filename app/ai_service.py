import google.generativeai as genai
from app.core.config import settings

def transcribe_audio(audio_bytes: bytes, mime_type: str) -> str:
    """
    Transcribes the given audio bytes using the Gemini AI API.

    Args:
        audio_bytes: The audio data in bytes.
        mime_type: The MIME type of the audio file.

    Returns:
        The transcription text.
    """
    if not settings.GOOGLE_API_KEY:
        raise ValueError("GOOGLE_API_KEY environment variable not set")

    genai.configure(api_key=settings.GOOGLE_API_KEY)

    model = genai.GenerativeModel('gemini-2.5-flash')

    audio_part = {
        "mime_type": mime_type,
        "data": audio_bytes
    }

    response = model.generate_content(
        ["Generate a transcript of the speech.", audio_part]
    )
    return response.text