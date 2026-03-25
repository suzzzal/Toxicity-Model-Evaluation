from models.base import BaseModel

class MockModel(BaseModel):
    """
    A simple mock model that flags text as toxic if it contains specific keywords.
    Useful for testing the evaluation pipeline without external dependencies.
    """
    
    def __init__(self):
        self.toxic_keywords = ["bad", "hate", "ugly", "stupid", "idiot", "jerk"]

    @property
    def name(self) -> str:
        return "MockKeywordModel"

    def predict(self, text: str) -> int:
        """
        Predicts 1 if any toxic keyword is in the text, otherwise 0.
        """
        text_lower = text.lower()
        if any(keyword in text_lower for keyword in self.toxic_keywords):
            return 1
        return 0
