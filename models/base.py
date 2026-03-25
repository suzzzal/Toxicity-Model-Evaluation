import abc

class BaseModel(abc.ABC):
    """
    Abstract base class for all toxicity models.
    Every model must implement the predict method.
    """
    
    @property
    @abc.abstractmethod
    def name(self) -> str:
        """Returns the name of the model."""
        pass

    @abc.abstractmethod
    def predict(self, text: str) -> int:
        """
        Predicts whether the given text is toxic.
        
        Args:
            text (str): The input text to evaluate.
            
        Returns:
            int: 1 if toxic, 0 if clean.
        """
        pass
