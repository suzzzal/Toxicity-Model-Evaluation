import time
import random
from models.base import BaseModel

class DetoxifyModel(BaseModel):
    """
    A local model placeholder (e.g., HuggingFace's Detoxify).
    Simulates local inference latency (slower than mock, faster than API).
    """
    
    def __init__(self):
        # Real implementation:
        # from detoxify import Detoxify
        # self.model = Detoxify('original')
        pass

    @property
    def name(self) -> str:
        return "Detoxify_Local_Mock"

    def predict(self, text: str) -> int:
        """
        Simulates local model inference.
        """
        # Simulate local CPU/GPU inference latency (50ms to 150ms)
        time.sleep(random.uniform(0.05, 0.15))
        
        # Real implementation:
        # results = self.model.predict(text)
        # return 1 if results['toxicity'] > 0.5 else 0
        
        # Simulated logic
        return 1 if len(text.split()) < 3 else 0
