from app.services.ml_model import VoiceSpoofDetector
from app.services.classifier import SimpleSpoofClassifier

_model = VoiceSpoofDetector()
_classifier = SimpleSpoofClassifier()

def detect_voice(signal, sr):
    if len(signal) < sr:  # < 1 second
        return {
            "prediction": "human",
            "confidence": 0.55,
            "explanation": "Audio too short for reliable spoof detection"
        }

    embedding = _model.extract_embedding(signal, sr)
    confidence_ai = _classifier.predict_proba(embedding)

    if confidence_ai >= 0.5:
        return {
            "prediction": "ai",
            "confidence": round(confidence_ai, 3),
            "explanation": "Voice embedding shows synthetic speech characteristics"
        }

    return {
        "prediction": "human",
        "confidence": round(1 - confidence_ai, 3),
        "explanation": "Voice embedding aligns with natural human speech patterns"
    }
