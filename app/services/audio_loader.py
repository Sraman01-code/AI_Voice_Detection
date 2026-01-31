import requests
import librosa
import io

TARGET_SR = 16000
MAX_DURATION_SEC = 8  # 👈 key fix

def load_audio_from_url(url: str):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        audio_bytes = io.BytesIO(response.content)

        signal, sr = librosa.load(
            audio_bytes,
            sr=TARGET_SR,
            mono=True,
            duration=MAX_DURATION_SEC  # 👈 LIMIT AUDIO
        )

        if len(signal) == 0:
            raise ValueError("Empty audio signal")

        return signal, TARGET_SR

    except Exception as e:
        raise ValueError(f"Audio loading failed: {str(e)}")
