import numpy as np

class SimpleSpoofClassifier:
    """
    Hand-calibrated lightweight classifier.
    Replaces with trained model later if needed.
    """

    def predict_proba(self, embedding: np.ndarray) -> float:
        energy = np.linalg.norm(embedding)

        # calibrated logistic curve
        score = 1 / (1 + np.exp(-0.0015 * (energy - 130)))

        return float(np.clip(score, 0.05, 0.95))

