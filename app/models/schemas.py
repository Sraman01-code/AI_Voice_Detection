from pydantic import BaseModel, HttpUrl, Field

class DetectRequest(BaseModel):
    audio_url: HttpUrl
    language: str | None = Field(default="en")

class DetectResponse(BaseModel):
    prediction: str = Field(pattern="^(ai|human)$")
    confidence: float = Field(ge=0.0, le=1.0)
    model_version: str
    explanation: str

    model_config = {
        "protected_namespaces": ()
    }


class GuviDetectRequest(BaseModel):
    language: str
    audio_format: str
    audio_base64: str
