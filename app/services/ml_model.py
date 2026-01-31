import torch
torch.set_num_threads(2)
import numpy as np
from transformers import Wav2Vec2Model, Wav2Vec2Processor

class VoiceSpoofDetector:
    def __init__(self):
        self.processor = Wav2Vec2Processor.from_pretrained(
            "facebook/wav2vec2-base"
        )
        self.model = Wav2Vec2Model.from_pretrained(
            "facebook/wav2vec2-base"
        )
        self.model.eval()

    @torch.no_grad()
    def extract_embedding(self, signal, sr):
        inputs = self.processor(
            signal,
            sampling_rate=sr,
            return_tensors="pt",
            padding=True
        )
        outputs = self.model(**inputs)
        hidden_states = outputs.last_hidden_state  # [T, 768]

        # Statistical pooling (important!)
        mean = hidden_states.mean(dim=1)
        std = hidden_states.std(dim=1)

        embedding = torch.cat([mean, std], dim=1)
        return embedding.squeeze().numpy()

