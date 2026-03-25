import time
from typing import List, Dict, Any
from models.base import BaseModel
from evaluator.metrics import calculate_accuracy, calculate_false_positive_rate, calculate_average_latency

class EvaluationRunner:
    """
    Executes toxicity model evaluations against a dataset and compiles metrics.
    """
    
    def __init__(self, dataset: List[Dict[str, Any]]):
        """
        Args:
            dataset: List of dictionaries containing {'text': str, 'label': int}
        """
        self.dataset = dataset

    def evaluate(self, model: BaseModel) -> Dict[str, Any]:
        """
        Evaluates a single model against the dataset.
        
        Args:
            model (BaseModel): The model instance to evaluate.
            
        Returns:
            Dict containing the model name, accuracy, latency, and FPR.
        """
        predictions = []
        labels = []
        latencies = []

        for sample in self.dataset:
            text = sample['text']
            label = sample['label']
            labels.append(label)

            # Measure latency per request
            start_time = time.time()
            try:
                pred = model.predict(text)
            except Exception as e:
                print(f"Error predicting with {model.name}: {e}")
                pred = 0 # Default to safe class on error
            
            latency_ms = (time.time() - start_time) * 1000
            
            predictions.append(pred)
            latencies.append(latency_ms)

        # Calculate metrics
        acc = calculate_accuracy(predictions, labels)
        fpr = calculate_false_positive_rate(predictions, labels)
        avg_latency = calculate_average_latency(latencies)

        return {
            "model": model.name,
            "accuracy": acc,
            "latency_ms": avg_latency,
            "false_positive_rate": fpr
        }
