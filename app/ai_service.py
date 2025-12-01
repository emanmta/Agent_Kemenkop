import google.generativeai as genai
from google.generativeai.types import Part
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
    if not settings.GEMINI_API_KEY:
        raise ValueError("GEMINI_API_KEY environment variable not set")

    genai.configure(api_key=settings.GEMINI_API_KEY)
    client = genai.Client()

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            "Generate a transcript of the speech.",
            Part.from_bytes(
                data=audio_bytes,
                mime_type=mime_type,
            )
        ]
    )
    return response.text