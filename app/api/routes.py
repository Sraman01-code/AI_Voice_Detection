from fastapi import APIRouter, Depends, HTTPException
from app.models.schemas import DetectRequest, DetectResponse
from app.core.security import verify_api_key
from app.core.config import MODEL_VERSION
from app.services.audio_loader import load_audio_from_url
from app.services.detector import detect_voice
from app.models.schemas import GuviDetectRequest
from app.services.audio_base64_loader import load_audio_from_base64
router = APIRouter()

@router.post("/detect", response_model=DetectResponse)
def detect(payload: DetectRequest, auth=Depends(verify_api_key)):
    try:
        signal, sr = load_audio_from_url(payload.audio_url)
        result = detect_voice(signal, sr)

        return DetectResponse(
            prediction=result["prediction"],
            confidence=result["confidence"],
            model_version=MODEL_VERSION,
            explanation=result["explanation"]
        )

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")



@router.post("/detect/guvi", response_model=DetectResponse)
def detect_guvi(
    payload: GuviDetectRequest,
    auth=Depends(verify_api_key)
):
    try:
        signal, sr = load_audio_from_base64(payload.audio_base64)
        result = detect_voice(signal, sr)

        return DetectResponse(
            prediction=result["prediction"],
            confidence=result["confidence"],
            model_version=MODEL_VERSION,
            explanation=result["explanation"]
        )

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
