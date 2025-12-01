# Audio Transcription API with FastAPI and Gemini AI

This project provides a simple API for transcribing audio files using FastAPI and Google's Gemini AI.

## Features

-   Upload audio files to a RESTful endpoint.
-   Transcribe speech from audio files into text.
-   Easy to set up and run.

## Setup and Installation

1.  **Clone the repository:**

    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **Install dependencies:**

    This project uses Poetry for dependency management. Make sure you have it installed.

    ```bash
    poetry install
    ```

3.  **Set up environment variables:**

    Create a `.env` file in the root of the project and add your Gemini API key:

    ```
    GEMINI_API_KEY="your_api_key_here"
    ```

## How to Run

1.  **Start the FastAPI server:**

    ```bash
    python manage.py
    ```

2.  **Access the API:**

    The API will be available at `http://0.0.0.0:8000`.

## API Usage

### Transcribe Audio

-   **Endpoint:** `/transcribe/`
-   **Method:** `POST`
-   **Body:** `multipart/form-data`
-   **Field:** `file` (the audio file to be transcribed)

**Example using `curl`:**

```bash
curl -X POST -F "file=@/path/to/your/audio.mp3" http://127.0.0.1:8000/transcribe/
```

**Example response:**

```json
{
  "transcription": "This is the transcribed text from the audio file."
}