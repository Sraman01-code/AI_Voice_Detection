import base64
import io
import librosa

TARGET_SR = 16000
MAX_DURATION_SEC = 8

def load_audio_from_base64(b64_string: str):
    try:
        audio_bytes = base64.b64decode(b64_string)
        audio_buffer = io.BytesIO(audio_bytes)

        signal, sr = librosa.load(
            audio_buffer,
            sr=TARGET_SR,
            mono=True,
            duration=MAX_DURATION_SEC
        )

        if len(signal) == 0:
            raise ValueError("Empty audio")

        return signal, TARGET_SR

    except Exception as e:
        raise ValueError(f"Invalid base64 audio: {str(e)}")

