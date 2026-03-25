import time
import random
from models.base import BaseModel

class OpenAIModeration(BaseModel):
    def __init__(self, api_key: str = None):
        self.api_key = api_key

    @property
    def name(self) -> str:
        return "OpenAI Moderation"

    def predict(self, text: str) -> int:
        time.sleep(random.uniform(0.1, 0.3))
        return 1 if ("hate" in text.lower() or "kill" in text.lower()) else 0


class GeminiSafety(BaseModel):
    def __init__(self, api_key: str = None):
        self.api_key = api_key

    @property
    def name(self) -> str:
        return "Gemini Safety"

    def predict(self, text: str) -> int:
        time.sleep(random.uniform(0.2, 0.4))
        return 1 if ("stupid" in text.lower() or "idiot" in text.lower()) else 0


class AzureContentSafety(BaseModel):
    def __init__(self, api_key: str = None):
        self.api_key = api_key

    @property
    def name(self) -> str:
        return "Azure AI Content Safety"

    def predict(self, text: str) -> int:
        time.sleep(random.uniform(0.15, 0.35))
        return 1 if ("ugly" in text.lower()) else 0


class AWSComprehend(BaseModel):
    def __init__(self, api_key: str = None):
        self.api_key = api_key

    @property
    def name(self) -> str:
        return "AWS Comprehend"

    def predict(self, text: str) -> int:
        time.sleep(random.uniform(0.25, 0.45))
        return 1 if ("jerk" in text.lower()) else 0


class PerspectiveAPI(BaseModel):
    def __init__(self, api_key: str = None):
        self.api_key = api_key

    @property
    def name(self) -> str:
        return "Perspective API"

    def predict(self, text: str) -> int:
        time.sleep(random.uniform(0.1, 0.2))
        return 1 if ("bad" in text.lower()) else 0

class DetoxifyAPI(BaseModel):
    def __init__(self):
        pass

    @property
    def name(self) -> str:
        return "Detoxify"

    def predict(self, text: str) -> int:
        time.sleep(random.uniform(0.05, 0.15))
        return 1 if len(text.split()) < 3 else 0
