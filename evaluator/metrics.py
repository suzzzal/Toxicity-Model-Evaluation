from typing import List

def calculate_accuracy(predictions: List[int], grounds_truth: List[int]) -> float:
    """
    Calculates accuracy as a percentage: (correct predictions / total) * 100
    """
    if not grounds_truth:
        return 0.0
    
    correct = sum(1 for p, g in zip(predictions, grounds_truth) if p == g)
    return round((correct / len(grounds_truth)) * 100, 2)

def calculate_false_positive_rate(predictions: List[int], grounds_truth: List[int]) -> float:
    """
    Calculates False Positive Rate as a percentage: (false positives / total true negatives) * 100
    A false positive occurs when prediction is 1 (toxic) but ground truth is 0 (clean).
    """
    false_positives = sum(1 for p, g in zip(predictions, grounds_truth) if p == 1 and g == 0)
    true_negatives = sum(1 for g in grounds_truth if g == 0)
    
    if true_negatives == 0:
        return 0.0
        
    return round((false_positives / true_negatives) * 100, 2)

def calculate_average_latency(latencies_ms: List[float]) -> float:
    """
    Calculates the average latency in milliseconds.
    """
    if not latencies_ms:
        return 0.0
    
    return round(sum(latencies_ms) / len(latencies_ms), 2)
